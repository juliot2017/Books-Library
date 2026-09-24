from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[schemas.BookResponse])
def get_all_books(db=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    books = db.query(models.Book).all()
    return books

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BookResponse)
def create_book(book_data: schemas.BookCreate, db=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    book = models.Book(**book_data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.put("/{id}", response_model=schemas.BookResponse)
def update_book(id: int, book_data: schemas.BookCreate, db=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book_data.model_dump().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

@router.get("/{id}", response_model= schemas.BookResponse)
def get_book(id: int, db=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return None