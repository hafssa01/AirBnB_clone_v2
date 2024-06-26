#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


# Note: BaseModel does NOT imherit from Base
# it only defines the common attributes
class BaseModel:
    """A base class for all hbnb models"""
    # define the field properties of the attributes (for sqlalchemy)
	@@ -56,7 +57,7 @@ def to_dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
