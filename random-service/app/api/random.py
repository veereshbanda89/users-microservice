from typing import List, Union
from fastapi import APIRouter, HTTPException, Header
import random
from app.utils.auth_utils import JWT_TOKEN_SECRET_KEY
import bcrypt
import jwt

random_service = APIRouter()

@random_service.get('/random')
async def create_users(header_token: Union[str, None] = Header(default=None)):
    token = header_token.replace("Bearer ", "")
    decoded = jwt.decode(token, JWT_TOKEN_SECRET_KEY, "HS256")
    if decoded.get('user_id') == "admin":
        # generating a random integer between 20000 and 50000
        random_value = random.randint(20000,50000)
        return {"value": random_value}
    else:
        return {"error_message" : "User is not authorized to access this resource with an explicit deny, regenerate the token"}
