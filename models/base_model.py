#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    
    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """Updates updated_at with the current time"""
        self.updated_at = datetime.utcnow()
        # Call storage save method here if needed
        # storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary.update({'__class__': self.__class__.__name__})
        return dictionary

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
