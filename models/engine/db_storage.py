#!/usr/bin/python3
"""Defines a class to manage file storage for hbnb clone"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """Definition of DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of DBStorage class"""
        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,)
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")
        if hb_env == "test":
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
