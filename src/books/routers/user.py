from fastapi import Depends, FastAPI, status, HTTPException, APIRouter
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def sign_up(user: schemas.UserCreate,db=Depends(get_db)):

     # Check whether the email already exists
    existing_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists"
        )

    #Hash the password - user.password
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    sign_up = models.User(**user.model_dump())
    db.add(sign_up)
    db.commit()
    db.refresh(sign_up)
    return sign_up

@router.get("/{id}", response_model = schemas.UserOut)
def get_user(id: int, db=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} not does not exist")
    return user
