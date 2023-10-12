from fastapi import APIRouter, Request, Depends, status, HTTPException
from server.authentication.jwt_bearer import JWTBearer
from server.authentication import jwt_handler
from server.authentication.bcrypter import Hasher
from server.models.account import (
  LogIn,
  Registration,
  Account,
  SubscriberAccount
)

router = APIRouter()

@router.post("/login",
             status_code=status.HTTP_200_OK,
             response_description="Successfully logged in.")
async def login(credentials: LogIn):
        try:
            account = await Account.find_one(Account.email == credentials.email)
            if account:
              verified = Hasher().verify_password(
                    login_password=credentials.password, member_password=account.password)
              
              if verified:
                  name = account.first_name + " " + account.last_name
                  token = jwt_handler.signJWT(str(account.id), name, account.role)
                  return token

            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="username or password is incorrect") 
        except Exception as e:

            if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="username or password is incorrect")
            
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="An error occured: " + str(e)) 

@router.post("/create",
             dependencies=[Depends(JWTBearer(access_level='admin'))],
             status_code=status.HTTP_201_CREATED,
             response_description="Account created"
            )
async def create_account(request: Request, account: Registration):
        try:
            account.created_by = request.state.user_details['name']
            if account.role != 'subscriber':
              new_account = Account(
                  first_name=account.first_name,
                  middle_name=account.middle_name,
                  last_name=account.last_name,
                  role=account.role,
                  email=account.email,
                  password=Hasher().hash_password(password=account.password),
                  created_by=account.created_by
              )
              
            else:
                new_account = SubscriberAccount(
                  first_name=account.first_name,
                  middle_name=account.middle_name,
                  last_name=account.last_name,
                  role=account.role,
                  school=account.school,
                  email=account.email,
                  password=Hasher().hash_password(password=account.password),
                  created_by=account.created_by
              )
                
            await new_account.insert()
            return {"detail": "Successfully Created Account",  "Account": new_account}
        except Exception as e:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="An error occured: " + str(e)) 
    
    