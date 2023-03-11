#!/usr/bin/python3
"""Saves objects in file to FileStorage class attribute __objects"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
