from fastapi import APIRouter, Request
from ..schema.user import UserRequest, UserUpdate
from ..model.user import UserModel
router = APIRouter()


@router.get("/users/{user_id}", tags=["users"])
async def read_users(user_id, request: Request):
    user_model = UserModel(request.state.db)
    user_data = user_model.get_by_id(user_id)
    user_data['_id'] = str(user_data['_id'])
    return {"user_data": user_data}


@router.post("/users/")
async def insert_users(users: UserRequest, request: Request):
    user_model = UserModel(request.state.db,request.state.db_image)
    user_id = user_model.insert(users)
    result = user_model.insert_profile_image(users, str(user_id))
    return {"message":"create user successfully.", "user_id": str(user_id)}
 
@router.put("/users/{user_id}")
async def update_users(users: UserUpdate, user_id, request: Request):
    user_model = UserModel(request.state.db)
    result = user_model.update(user_id,users)
    return {"message":"update user successfully."}

@router.delete("/users/{user_id}")
async def delete_users(user_id, request: Request):
    user_model = UserModel(request.state.db)
    result = user_model.delete(user_id)
    return {"message": "delete user successfully."}
