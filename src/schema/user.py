from typing import Optional, Any
from pydantic import BaseModel, validator
import pybase64 as base64
from io import BytesIO
from PIL import Image
class UserBase(BaseModel):
    name: str  #validate eng name not empty
    surname: str #validate eng surname not empty
    telephone: str #validate only number
    find_mate: bool 
    description: Optional[str] = '' 
    user_type: str #validate type owner renter
class UserRequest(UserBase):
    image: Optional[Any] = None #validate str utf8 base64
    @validator('image')
    def validate_image(cls, v):
        if not isinstance(v, str):
            raise ValueError('Image format does not correct.')
        try:
            img_str = base64.b64decode(v.encode('utf-8'))
            buf = BytesIO(img_str)
            img = Image.open(buf)
            return img
        except Exception as e:
            print(e)
            raise ValueError('Image format does not correct.')
class User(UserBase):
    image: str
    created_at: float
    updated_at: float

class UserUpdate(UserRequest):
    pass


