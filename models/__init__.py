#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
=======
from models.engine.file_storage import FileStorage


storage = FileStorage()
>>>>>>> 9451faf353cb54245875401b7b00ac303fc3ea71
storage.reload()
