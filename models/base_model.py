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
