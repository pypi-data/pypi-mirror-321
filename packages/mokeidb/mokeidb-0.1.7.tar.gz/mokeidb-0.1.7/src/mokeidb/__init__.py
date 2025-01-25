"""mokeidb

By deuxglaces
"""
import pathlib

import mokeidb.mongodb
from mokeidb.enum import EnumMixin
from mokeidb.exceptions import DatabaseError, UniqueConflict, NoDatabase
from mokeidb.decorators import collection, database
from mokeidb.generics import Key, Unique, NotNull
from mokeidb.mongodb import MongoDbModel, mongodb_config
from mokeidb.sqlite import SqliteDbModel

__version__ = '0.1.7'
