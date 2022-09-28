from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# tokenUrl is the "relative" endpoint to get token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/")
async def hello():
    return {"msg": "Hello this is API server"}


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
