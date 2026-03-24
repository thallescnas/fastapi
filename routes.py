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
def post_user(user: User):
    user_dic = user.model_dump()
    result = users_collection.insert_one(user_dic)
    
    return{
        "message": {"User created"},
        "id": str(result.inserted_id)
    }
@router.get("/users/{user_id}")
def get_usr(user_id: str):
    for user in list_users():
     if str(user["_id"]) == user_id:
        return user
    return {"error": "202 user not found"}

@router.delete("/users/delete/{user_id}")
def delete_usr(user_id):
   #arrumar
   for user in list_users():
      if str(user["_id"]) == user_id:
         users_collection.delete_one(user)
         return {"message": "sucess"}