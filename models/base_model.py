#!/usr/bin/env python3
"""
A class model that defines all common attributes/methods
for other class

"""
import uuid
import datetime

class BaseModel:
    """BaseModel class to be inherited by other classes"""
    def __init__(self, *args, **kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            if Kwargs is not None:
                if '__class__' in kwargs:
                    continue
    def __setattr__(self, name, value):
        # Name and Value attribute to be set here ...
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.name, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = dict(self.__dict__)
        dic.update({'__class__': self.__class__.name
                'created_at': isoformat()
                'updated_at': isoformat()
                })
        return dic
