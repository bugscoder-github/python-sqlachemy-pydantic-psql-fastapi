from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr
from typing import Optional
from db.db_connection import Base

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr

class UserSchema(BaseModel):
    name: Optional[int] = None
    type: str

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    type = Column(String, default="Pending")
    about = Column(String, nullable=True)
    resume = Column(String, nullable=True)
    resume_base64 = Column(String, nullable=True)

    skills = relationship('UserSkills', back_populates='user', lazy="joined")


class UserSkills(Base):
    __tablename__ = "users_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    user = relationship('User', back_populates='skills')