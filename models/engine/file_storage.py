#!/usr/bin/python3
"""
 A file storage that serializes instances to a
 JSON file and deserializes JSON file to instances

 """
 import json
 import models
 from 
 class FileStorage():
     __file_path = "file.json"
     __objects = {}

     def all(self):
         return self.__objects
     def new(self, obj):
         key = obj.__class__.__name__ + "." + obj.id
         self.__objects[key] = obj

     def save(self):
         """ serializes __objects to the JSON file """
         with open(self.__file_path, 'w') as f:
             dct = {}
             for name, obj in self.__objects.items():
                 dct[name] = obj.to_dict()
             json.dump(dct, f)
     def reload(self):
           """ deserializes __objects to the JSON file """
         try:
             with open(self.__file_path, 'r') as f:
                 jsdic = json.load(f.read())
