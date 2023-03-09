#!/usr/bin/python3
"""
 A file storage that serializes instances to a
 JSON file and deserializes JSON file to instances

 """
 import json
 import models

 class FileStorage():
     __file_path = str(file.json)
     __objects = dict()

     def all(self):
         return self.__objects
     def new(self, obj):
         key = obj.__class__.__name__ + "." + obj.id
         self.__objects[key] = obj

     def save(self):

         with open('__file_path', 'w') as f:
             dct = dict()
             for name, obj in self.__objects.items():
                 dct[name] = obj.to_dict()
             json.dump(dct, f)
