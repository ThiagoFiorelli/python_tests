from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
import re


Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id_ = Column('id', Integer, primary_key = True)
    name = Column('name', String(length=100), nullable = False)
    description = Column('description', String(length=255), nullable = True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string!')
        if not name.strip():
            raise ValueError('Name cannot be empty!')
        if len(name) > 100:
            raise ValueError('Name must be 100 or less characters!')
        if not re.match(r'^[a-zà-úA-ZÀ-Ú0-9,. ]+$', name):
            raise ValueError('Name cannot have special characters!')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str) and description is not None:
            raise TypeError('Description must be a string!')
        if len(description) > 255:
            raise ValueError('Description must be 255 or less characters!')
        return description

