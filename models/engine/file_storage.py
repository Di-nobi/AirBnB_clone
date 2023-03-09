#!/usr/bin/python3
"""
 A file storage that serializes instances to a
 JSON file and deserializes JSON file to instances

 """
 import json
 import models
<<<<<<< HEAD
 from models.base_model import BaseModel
 class FileStorage():
     __file_path = 'file.json'
=======
 from 
 class FileStorage():
     __file_path = "file.json"
>>>>>>> f91f009388c3c7ae00c1de83a3064517a5815ba2
     __objects = {}

     def all(self):
         return self.__objects
     def new(self, obj):
         key = obj.__class__.__name__ + "." + obj.id
         self.__objects[key] = obj

     def save(self):
<<<<<<< HEAD
         """ serializing to get json files """
=======
         """ serializes __objects to the JSON file """
>>>>>>> f91f009388c3c7ae00c1de83a3064517a5815ba2
         with open(self.__file_path, 'w') as f:
             dct = {}
             for name, obj in self.__objects.items():
                 dct[name] = obj.to_dict()
             json.dump(dct, f)
<<<<<<< HEAD

     def reload(self):
         """ deserializing to get json files """
         try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f,)
=======
     def reload(self):
           """ deserializes __objects to the JSON file """
         try:
             with open(self.__file_path, 'r') as f:
                 jsdic = json.load(f.read())
>>>>>>> f91f009388c3c7ae00c1de83a3064517a5815ba2
