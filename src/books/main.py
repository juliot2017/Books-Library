from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from httpx import post


from . import database

from .database import SessionLocal
from .schemas import  BookResponse
from src.books import models, schemas, utils
from .routers import book, user, auth

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(book.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}






