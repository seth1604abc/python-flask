from model.userModel import User
from pydantic import BaseModel
from sqlalchemy.orm import Session

class create_user_dto(BaseModel):
    name: str
    username: str
    password: str
    db_session: Session

class UserRepository:
    @staticmethod
    def get_by_username(username: str):
        return User.query.filter_by(username == username).first()
    
    @staticmethod
    def create_user(dto: create_user_dto):
        new_user = User(name=dto.name, username=dto.username, password=dto.password)
        dto.db_session.add(new_user)
        dto.db_session.commit()