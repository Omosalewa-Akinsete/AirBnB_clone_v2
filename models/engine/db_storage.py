#!/usr/bin/python3
"""Defines a class to manage file storage for hbnb clone"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """Definition of DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage class"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(getenv("HBNB_MYSQL_USER"),getenv("HBNB_MYSQL_PWD"),getenv("HBNB_MYSQL_HOST"),getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)


    def reload(self):
        """Define reload method"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None, id=None):
        """Define all method"""
        allClasses = [User, State, City, Amenity, Place, Review]
        result = {}

        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
            else:
                for obj in self.__session.query(cls).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + str(obj.id)
                    result[keyName] = obj
        else:
            for clss in allClasses:
                if id is not None:
                    obj = self.__session.query(clss).get(id)
                    if obj is not None:
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
        return result

    def search(self, cls, id):
        """Define search method"""
        data = self.all(cls)

    def new(self, obj):
        """Define new method"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Define save method"""
        self.__session.commit()

    def delete(self, obj=None):
        """Define delete method"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Define close method"""
        self.__session.close()
