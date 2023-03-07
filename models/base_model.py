#!/usr/bin/env python3
"""
A class model that defines all common attributes/methods
for other class

"""
import uuid
import datetime

class BaseModel:
    """BaseModel class to be inherited by other classes"""
    def __init__(self, id, created_at, updated_at):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.name, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        dic = dict(self.__dict__)
        dic = {'__class_': self.__class__.name
                'created_at': isoformat()
                'updated_at': isoformat()
                }
        return dic
