# services/user_service.py

from sqlalchemy.orm import Session
from ..models.UserModel import User
from ..schemas.UserSchema import UserCreate, UserUpdate


class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def list_users(db: Session, skip: int = 0, limit: int = 10):
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def update_user(db: Session, user_id: int, user: UserUpdate) -> User:
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            return None

        for key, value in user.model_dump().items():
            setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(db: Session, user_id: int) -> User:
        db_user = UserService.get_user_by_id(db, user_id)
        if not db_user:
            return None

        db.delete(db_user)
        db.commit()
        return db_user
