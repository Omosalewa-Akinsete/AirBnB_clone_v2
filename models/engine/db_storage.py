#!/usr/bin/python3
""" Module that creates a new engine named `db_storage.py`"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DBStorage class for managing database storage"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """ init special method """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        db_url = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        if os.getenv('HBNB_ENV') == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)
        self.__engine = create_engine(db_url, pool_pre_ping=True)

    def all(self, cls=None):
        """method  that query all list of models files"""
        if cls is not None:
            data = self.__session.query(cls)
        else:
            new_classes = [State, City, User, Place, Review]
            data = []
            for loop in new_classes:
                data.extend(self.__session.query(itter).all())
        obj_dic = {}
        for obj in data:
            classname = type(obj).__name__
            id = obj.id
            key = f"{classname}.{id}"
            obj_dic[key] = obj
            return obj_dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        """ This method commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session obj if not None """
        if (obj):
            self.__session.delete(obj)

    def reload(self):
        from models.user import User, Base
        from models.user import User, Base
        from models.place import Place, Base
        from models.state import State, Base
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

