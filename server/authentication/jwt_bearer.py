from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from server.authentication import jwt_handler


class JWTBearer(HTTPBearer):
    def __init__(
        self,
        access_level: str,
        auto_error: bool = True,
    ):
        self.access_level = access_level
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        credentials.credentials = credentials.credentials.replace('"', "")

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )

            verification = self.verify_jwt(credentials.credentials, self.access_level)

            if not verification:
                raise HTTPException(status_code=403, detail="Invalid token")

            request.state.user_details = jwt_handler.decodeJWT(
                credentials.credentials, self.access_level
            )

            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str, access_level: str) -> bool:
        isTokenValid = False

        try:
            payload = jwt_handler.decodeJWT(jwtoken, access_level)
        except:
            payload = None

        if payload and "error" in payload:
            if payload["error"] == "unauthorized":
                raise HTTPException(status_code=403, detail="Access denied")
            if payload["error"] == "token expired":
                raise HTTPException(status_code=403, detail="Token expired")
        if payload:
            isTokenValid = True

        return isTokenValid
