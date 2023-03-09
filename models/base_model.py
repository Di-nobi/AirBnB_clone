#!/usr/bin/python3
"""
A class model that defines all common attributes/methods
for other class

"""
import uuid
from datetime import datetime

class BaseModel():
    """BaseModel class to be inherited by other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if kwargs == '__class__':
                    continue
                elif kwargs == 'created_at' or kwargs == 'updated_at':
                    self.__dict__[key] = datetime.isoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    def __str__(self):
        """Format `self` for output"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """returns a dictionary containing all key/value pairs of __dict__"""
        dic = dict(self.__dict__.copy())
        dic.update({'__class__': self.__class__.__name__,
                'created_at': self.created_at.isoformat(),
                'updated_at': self.updated_at.isoformat()
                })
        return dic
