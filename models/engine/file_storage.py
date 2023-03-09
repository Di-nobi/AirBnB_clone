#!/usr/bin/python3
"""
 A file storage that serializes instances to a
 JSON file and deserializes JSON file to instances

 """
 import json

 class FileStorage():
     __file_path = str(file.json)
     __objects = dict()

     def all(self):
         return self.__objects
     def new(self):
         key = obj.__class__.__name__ + "." + obj.id
         self.__objects[key] = obj


