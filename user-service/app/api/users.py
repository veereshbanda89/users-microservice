from typing import List, Union
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from app.utils.auth_utils import generate_jwt_token, hash_password
from __init__ import firestore_db
from app.utils.auth_utils import JWT_TOKEN_SECRET_KEY
users_collection = firestore_db.collection("users")
import datetime
import bcrypt
import jwt

users = APIRouter()

class User(BaseModel):
    username: str
    password: str

@users.post('/auth/login')
async def login_user(item: User):
    docs = users_collection.where(
            "username", "==", item.username).stream()
    data = dict()
    for user in docs:
        user_dict = user.to_dict()

        if item.username == user_dict.get("username") and item.password == user_dict.get("password"):
            data.update({'username': item.username})
            data.update({'access_token': generate_jwt_token(item.username)})

    return {"username": data.get('username'), "access_token": data.get('access_token')}

@users.post('/create-users')
async def create_users(users: List[User],header_token: Union[str, None] = Header(default=None)):
    token = header_token.replace("Bearer ", "")
    decoded = jwt.decode(token, JWT_TOKEN_SECRET_KEY, "HS256")
    previous_time = datetime.datetime.now()
    if decoded.get('user_id') == "admin":
        for user in users:
            docs = (users_collection.where("username", "==", user.username).stream())
            for doc in docs:
                current_time = datetime.datetime.now()
                if current_time > previous_time:
                    string_username = doc.to_dict().get("username")
                    string_password = doc.to_dict().get("password")
                    user_data = string_username + "," + string_password

                    file1 = open("backup.txt","w")
                    l = list(user_data)
                    file1.writelines(l)
                    file1.close()
                    previous_time = current_time
                # if user.get("username") == doc.to_dict().get("username"):
                #     return {"error_messsage": "Member with this username already exists"}
            data = {
                "username": user.username,
                "password": hash_password(user.password)
            }
            users_collection.add(data)
        return {"message": "resources created successfully!"}
    else:
        return {"error_message" : "User is not authorized to access this resource with an explicit deny, regenerate the token"}
    return {"username": users, "header_token": header_token, "decoded": decoded}


@users.get('/get-users')
async def get_users(page: int = 0, size: int = 10, header_token: Union[str, None] = Header(default=None), username: Union[str, None] = None):
    token = header_token.replace("Bearer ", "")
    decoded = jwt.decode(token, JWT_TOKEN_SECRET_KEY, "HS256")
    if decoded.get('user_id') == "admin":
        docs = (users_collection.where("username", "==", username).stream())
        users_list = []
        for doc in docs:
            if username == doc.to_dict().get("username"):
                users_list.append(username)
        if len(users_list)>0:
            return {"username": users_list}
        else:
            return {"error_message" : "Username not found"}
    else:
        return {"error_message" : "User is not authorized to access this resource with an explicit deny, regenerate the token"}
    return {"username": users, "header_token": header_token, "decoded": decoded}
    
