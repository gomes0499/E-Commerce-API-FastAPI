# api/routes/user_route.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ...core.database import SessionLocal
from ...schemas.UserSchema import UserBase, UserCreate, UserUpdate
from ...services.UserService import UserService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)


@router.get("/users/{user_id}", response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserService.get_user_by_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/")
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return UserService.list_users(db, skip, limit)


@router.put("/users/{user_id}", response_model=UserBase)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = UserService.update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", response_model=UserBase)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserService.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
