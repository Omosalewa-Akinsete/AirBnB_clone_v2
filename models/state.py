#!/usr/bin/python3
""" State Module for HBNB project """
import models
import os
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if genenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Gets a list of cities"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
                return city_list
