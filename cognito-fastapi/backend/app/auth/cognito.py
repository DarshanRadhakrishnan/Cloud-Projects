import requests
from jose import jwt
from jose.exceptions import JWTError
from fastapi import HTTPException, status
import os

AWS_REGION = os.getenv("AWS_REGION")
USER_POOL_ID = os.getenv("USER_POOL_ID")
APP_CLIENT_ID = os.getenv("APP_CLIENT_ID")

COGNITO_ISSUER = f"https://cognito-idp.{AWS_REGION}.amazonaws.com/{USER_POOL_ID}"
JWKS_URL = f"{COGNITO_ISSUER}/.well-known/jwks.json"

jwks = requests.get(JWKS_URL).json()

def verify_token(token: str):
    try:
        headers = jwt.get_unverified_header(token)
        key = next(k for k in jwks["keys"] if k["kid"] == headers["kid"])

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            audience=APP_CLIENT_ID,
            issuer=COGNITO_ISSUER
        )
        return payload

    except StopIteration:
        raise HTTPException(status_code=401, detail="Invalid token key")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token verification failed")
