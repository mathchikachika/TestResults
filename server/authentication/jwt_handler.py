import json
import time
from typing import Dict

import cryptocode
from jose import jwt

PAYLOAD_SECRET = "ubF5I41SuaVY2wmTnz43qA"
JWT_SECRET = "3a2c3158a8a428c1a0c1998360f7e452"
JWT_ALGORITHM = "HS256"


def token_response(token: str):
    return {"access_token": token}


def encodePayload(payload):
    converted = json.dumps(payload)
    encoded_text = cryptocode.encrypt(converted, PAYLOAD_SECRET)
    return encoded_text


def decodePayload(payload):
    decoded = cryptocode.decrypt(payload, PAYLOAD_SECRET)
    return decoded


def signJWT(uuid: str, name: str, role: str) -> Dict[str, str]:
    expiration_duration = 60 * 60 * 24
    data = {
        "uuid": uuid,
        "name": name,
        "role": role,
        "expires": time.time() + expiration_duration,
    }

    payload = {"data": encodePayload(data)}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str, access_level: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        decoded_payload = json.loads(decodePayload(decoded_token["data"]))

        if decoded_payload["expires"] >= time.time():
            if access_level == "staff" or access_level == "teacher":
                if decoded_payload["role"] == "teacher" and access_level == "teacher":
                    return decoded_payload
                elif (
                    decoded_payload["role"] == "subscriber"
                    and access_level == "subscriber"
                ):
                    return decoded_payload
                elif (
                    decoded_payload["role"] == "admin"
                    or decoded_payload["role"] == "staff"
                ):
                    return decoded_payload
                else:
                    return {"error": "unauthorized"}
            elif access_level == "admin":
                if decoded_payload["role"] == "admin":
                    return decoded_payload
                else:
                    return {"error": "unauthorized"}
            else:
                return decoded_payload
        else:
            return {"error": "token expired"}
    except Exception as e:
        return {}
