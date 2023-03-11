#!/usr/bin/python3
"""
 A file storage that serializes instances to a
 JSON file and deserializes JSON file to instance
"""
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    def save(self):
        """ serializing to get json files """
        with open(self.__file_path, 'w') as f:
            dct = {}
            for name, obj in self.__objects.items():
                dct[name] = obj.to_dict()
                json.dump(dct, f)
    def reload(self):
        """ deserializing to get json files """
        try:
            with open(self.__file_path) as f:
                dct = json.load(f)

                for key, value in dct.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'State':
                        FileStorage.__objects[key] = State(**value)
                    elif value['__class__'] == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    elif value['__class__'] == 'City':
                        FileStorage.__objects[key] = City(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
                    elif value['__class__'] == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value['__class__'] == 'Review':
                        FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            return
