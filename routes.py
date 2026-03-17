from fastapi import APIRouter
from database import users_collection
from schemas import User

router = APIRouter()

@router.get("/users")
def list_users():

    users = []

    for user in users_collection.find():

        user["_id"] = str(user["_id"])

        users.append(user)

    return users

@router.post("/users/create")
def post_user(usinho: User):
    for user in list_users:
        if user
