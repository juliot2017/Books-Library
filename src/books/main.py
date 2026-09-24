import time

from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from httpx import post

from . import database

from .database import SessionLocal
from .schemas import  BookResponse
import psycopg2
from psycopg2.extras import RealDictCursor
from src.books import models, schemas, utils
from .routers import book, user, auth

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_password: str = "localhost"
    database_username:str = "postgres"
    secret_key: str = "23ui2buhji"

settings = Settings()


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


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="bookly",
            user="postgres",
            password="Password123", cursor_factory=RealDictCursor
        )
        print("Database connection was successful!")
        break

    except Exception as error:
        print(f"Connection to database failed")
        print("Error: error")
        time.sleep(2)



@app.get("/")
def read_root():
    return {"Hello": "World"}






