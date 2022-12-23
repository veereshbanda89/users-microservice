import datetime
import bcrypt
import jwt

JWT_TOKEN_SECRET_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3MTU2NDU5MCwiaWF0IjoxNjcxNTY0NTkwfQ.j_BdU6OXDg0ODVR5h2e9LhaUYMX7TISRVg6pUHa1YAo"

def generate_jwt_token(user_id: str):
    time_now = datetime.datetime.now(tz=datetime.timezone.utc)
    expire_time = time_now + datetime.timedelta(minutes=60)
    token_data = {
        "user_id": user_id,
        "iat": time_now,
        "exp": expire_time,
    }
    encoded_token = jwt.encode(token_data, JWT_TOKEN_SECRET_KEY, "HS256")
    if isinstance(encoded_token, str):
        return encoded_token
    else:
        return encoded_token.decode('utf-8')

def hash_password(password: str):
    byte_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(byte_password, salt)
    return str(hashed_password.decode('utf-8'))