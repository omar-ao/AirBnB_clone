#!/usr/bin/python3
"""The ``__init__`` module
"""


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
