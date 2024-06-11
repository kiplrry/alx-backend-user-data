#!/usr/bin/env python3
"""user model implementaion with sqlalchemy
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Column

Base = declarative_base()


class User(Base):
    """User class
        impl
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    # def __init__(self, email, hashed_password, session_id=None,
    #              reset_token=None):
    #     self.email = email
    #     self.hashed_password = hashed_password
    #     self.session_id = session_id
    #     self.reset_token = reset_token
