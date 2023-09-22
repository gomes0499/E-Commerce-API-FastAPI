from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.UserModel import User
from app.schemas.UserSchema import UserBase, UserCreate, UserUpdate
from app.core.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(get_db())):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db())):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/")
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db())):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


router.put("/users/{user_id}", response_model=UserBase)


def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db())):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict().items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/users/{user_id}", response_model=UserBase)
def delete_user(user_id: int, db: Session = Depends(get_db())):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return db_user
