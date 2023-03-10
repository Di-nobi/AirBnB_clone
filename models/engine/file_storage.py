#!/usr/bin/python3
"""
 A file storage that serializes instances to a
 JSON file and deserializes JSON file to instance
"""
import json
import models
from models.base_model import BaseModel
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
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
