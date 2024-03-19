#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """
    __tablename__ = "state"
    if storage_type = "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""
        # Done: for FileStorage: getter attribute cities that returns the list
        # of City instance with state_id equals to the current State.id=> It
        # will be the FileStorage relationship between State and City

        @property
        def cities(self):
            """Cities getter"""
            from models import storage
            citiesList = []
            citiesAll = storage.all(City)
            for city in citiesAll.values():
                if city.state_id == self.id:
                    citiesList.append(City)
            return citiesList
