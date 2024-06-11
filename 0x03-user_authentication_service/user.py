#!/usr/bin/env python3
"""user model implementaion with sqlalchemy
"""
from typing import Optional
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column

Base = declarative_base()


class User(Base):
    """User class
        impl
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: Optional[str] = Column(String(250), nullable=True)
    reset_token: Optional[str] = Column(String(250), nullable=True)

    # def __init__(self, email, hashed_password, session_id=None,
    #              reset_token=None):
    #     self.email = email
    #     self.hashed_password = hashed_password
    #     self.session_id = session_id
    #     self.reset_token = reset_token
