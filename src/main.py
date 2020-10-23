from fastapi import Depends, FastAPI, Header, HTTPException,Request
from .router import user
from .model.db_client import DBClient
from .model.db_image import DBImage
app = FastAPI()
db = DBClient()
db_image = DBImage()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request.state.db = db
    request.state.db_image = db_image
    response = await call_next(request)
    return response

app.include_router(user.router)
