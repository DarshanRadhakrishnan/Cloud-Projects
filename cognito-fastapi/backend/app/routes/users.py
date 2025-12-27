from fastapi import APIRouter, Depends
from ..auth.dependancies import get_current_user


router = APIRouter()

@router.get("/me")
def get_profile(user=Depends(get_current_user)):
    return {
        "user_id": user["sub"],
        "email": user.get("email"),
        "username": user.get("cognito:username")
    }
