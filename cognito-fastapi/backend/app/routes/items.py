from fastapi import APIRouter, Depends
from app.auth.dependancies import get_current_user
from app.services.dynamodb import table

router = APIRouter()

@router.post("/")
def create_item(item: dict, user=Depends(get_current_user)):
    item["user_id"] = user["sub"]
    table.put_item(Item=item)
    return {"message": "Item saved"}

@router.get("/")
def get_items(user=Depends(get_current_user)):
    response = table.scan()
    return response.get("Items", [])
