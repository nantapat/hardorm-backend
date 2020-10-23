from ..schema.user import UserRequest, UserUpdate
from bson.objectid import ObjectId
import time 
from io import BytesIO
class UserModel():
    def __init__(self,db,db_image=None):
        self.db = db
        self.db_image = db_image
    def insert(self,user: UserRequest):
        user_dict = user.__dict__.copy()
        user_dict.pop('image', None)
        user_dict['created_at'] = time.time()
        user_dict['updated_at'] = time.time()
        return self.db.get_user_collection().insert_one(user_dict).inserted_id
    def get_by_id(self, id):
        return self.db.get_user_collection().find_one({'_id':ObjectId(id)})
    def update(self,id, user: UserUpdate):
        user_dict = user.__dict__.copy()
        user_dict['updated_at'] = time.time()
        return self.db.get_user_collection().update_one({'_id':ObjectId(id)},{ "$set": user_dict})
    def delete(self,id):
        return self.db.get_user_collection().delete_one({'_id':ObjectId(id)})
    
    def insert_profile_image(self, user: UserRequest, user_id):
        if(self.db_image is None):
            return None
        buffer = BytesIO()
        user_dict = user.__dict__.copy()
        image = user_dict.pop('image', None)
        if image is None:
            return None
        image.save(buffer, format="JPEG")
        nb_bytes = buffer.tell()
        buffer.seek(0)
        return self.db_image.insert_to_minio_server(user_id,buffer,nb_bytes)
        