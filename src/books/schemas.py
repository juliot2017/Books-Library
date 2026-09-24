from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, List


class BookBase(BaseModel):
    title: str
    author: str
    description: str


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    model_config = ConfigDict(from_attributes=True)

class UserOut(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)    

class UserLogin(BaseModel):
    email: EmailStr
    password: str 

class Token(BaseModel):
    access_token: str
    token_type: str       

class TokenData(BaseModel):
    id: int

class EmailModel(BaseModel):
    emails: List[str]    