from fastapi import APIRouter, Request, Depends, status, HTTPException, Body
from typing import Any
import math
from bson import ObjectId
from server.authentication.jwt_bearer import JWTBearer
from server.authentication import jwt_handler
from server.authentication.bcrypter import Hasher
from server.connection.database import db
from server.models.utilities import sample_payloads, model_parser
from server.models.validators.query_params_validators import validate_query_params
from server.models.account import (
  LogIn,
  Registration,
  Account,
  AccountResponseModel,
  SubscriberAccount,
  UpdatedPassword
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
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e)) 
        

@router.post("/register_emails",
             status_code=status.HTTP_200_OK,
             response_description="Successfully registered the emails.")
async def register_emails(credentials: LogIn):
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
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e)) 


@router.get("/user_data", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def get_user_data(request: Request, account_id: str = None):
    if account_id:
        sample = JWTBearer(access_level='admin')
        await sample.__call__(request)
    else:
        account_id = request.state.user_details['uuid']

    try:
        account = await Account.find({"_id":ObjectId(account_id) }).project(AccountResponseModel).to_list(None)
        return account
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
            
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.put("/update_details", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def update_account_details(request: Request,
                        account_id: str = None,
                        updated_account: Any = Body(openapi_examples=sample_payloads.updated_account_payload)):
    
    updated_account = model_parser.updated_account_parser(updated_account)
    updated_account.updated_by = request.state.user_details['name']
    if account_id:
      sample = JWTBearer(access_level='admin')
      await sample.__call__(request)
    else:
      account_id = request.state.user_details['uuid']

    try:
      fetched_account = await Account.get(account_id)
      if fetched_account:
          account = await fetched_account.update(
                          {"$set": updated_account.dict()}
                    )
          return {"Successfully updated": account}
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
            
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.put("/change_password", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def change_password(request: Request, updated_password: UpdatedPassword, account_id: str = None, ):
    
    updated_password.updated_by = request.state.user_details['name']
    if account_id:
      sample = JWTBearer(access_level='admin')
      await sample.__call__(request)
    else:
      account_id = request.state.user_details['uuid']

    try:
        fetched_account = await Account.get(account_id)

        if fetched_account:
            verified = Hasher().verify_password(
                    login_password=updated_password.old_password, member_password=fetched_account.password)
            if verified:
                updated_password = updated_password.model_dump()
                del updated_password['old_password']
                del updated_password['repeat_new_password']
                updated_password['password'] = Hasher().hash_password(updated_password['new_password'])
                del updated_password['new_password']

                await fetched_account.update(
                                {"$set": updated_password}
                          )
                
                return {"message": "Successfully change password"}
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Wrong password")
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
        
        if str(e) == '400':
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Wrong password") 
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
    
@router.put("/reset_password/{user_id}", dependencies=[Depends(JWTBearer(access_level='staff'))], status_code=status.HTTP_200_OK)
async def reset_password(request: Request, updated_password: UpdatedPassword, user_id: str = None, ):
    
    updated_password.updated_by = request.state.user_details['name']
    if user_id:
      sample = JWTBearer(access_level='admin')
      await sample.__call__(request)
    else:
      user_id = request.state.user_details['uuid']

    try:
        fetched_account = await Account.get(user_id)

        if fetched_account:
            verified = Hasher().verify_password(
                    login_password=updated_password.old_password, member_password=fetched_account.password)
            if verified:
                updated_password = updated_password.model_dump()
                del updated_password['old_password']
                del updated_password['repeat_new_password']
                updated_password['password'] = Hasher().hash_password(updated_password['new_password'])
                del updated_password['new_password']

                await fetched_account.update(
                                {"$set": updated_password}
                          )
                
                return {"message": "Successfully change password"}
            
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Wrong password")
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 
        
        if str(e) == '400':
                raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="Wrong password") 
        
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))

@router.delete("/delete/{user_id}", dependencies=[Depends(JWTBearer(access_level='admin'))], status_code=status.HTTP_200_OK)
async def delete_account(user_id: str):
    try:
      deleted_account = await db['account_collection'].find_one_and_delete({"_id": ObjectId(user_id)})
      if deleted_account:
          return {"detail": "Successfully Deleted Account"}

      raise HTTPException(status.HTTP_404_NOT_FOUND,
                          detail="Account not found") 
    except Exception as e:
        if str(e) == '404':
                raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail="Account not found") 

        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                detail="An error occured: " + str(e))
