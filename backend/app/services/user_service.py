from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserData


class UserService():
    @staticmethod
    async def get_users(db: Session):
        return db.query(User).all()
    
    @staticmethod
    async def get_user_by_id( db: Session, id: int):
        return db.query(User).filter(User.id == id).first()
    
    @staticmethod
    async def get_user_by_username( db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    async def create_user(db: Session, user: UserData):
        if not user.username:
            return None
        if not user.password:
            return None
        
        fake_pass = user.password + "#fake" # Simula encriptación
        new_user = User(username=user.username, password=fake_pass)

        db.add(new_user)
        db.commit()
        db.flush(new_user)

        return new_user