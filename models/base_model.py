#!/usr/bin/python3
"""Module `base_model.py` that creates output in a dictionary"""
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """Class BaseModel for overall hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Special Instance of class BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_ar = datetime.now()
        if kwargs:
            time_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, time_format)
                if hasattr(self, key):
                    setattr(self, key, value)
    def __str__(self):
        """ Returns a string representation format of a string """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Always save the time when instance is changed"""
        self.updated_at = datetime.utcnow()
        model.storage.new(self)
        model.storage.save()

    def to_dict(self):
        """_sa_instance_state manage instance of an ORM library"""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict.update({'__class__':
            (str(type(self)).split('.')[-1]).split('\'')[0]})
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        if 'sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        """Remove the current instance from the storage"""
        from models import storage
        storage.delete()
