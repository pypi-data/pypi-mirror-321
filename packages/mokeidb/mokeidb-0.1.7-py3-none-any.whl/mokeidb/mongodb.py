import collections.abc
import inspect
import os
import pathlib
import weakref
from typing import Self, Optional, Callable

import bson
import pymongo.database
import pymongo.errors

from .dbmodel import DbModel
from .exceptions import MultipleKeys, NoCollection, NoDatabase, UniqueConflict
from .generics import Key, Unique
from .serializer import Serializer


def register_type(type_, store_fn: collections.abc.Callable, retrive_fn: collections.abc.Callable):
    MongoDbModel.register_type(type_, store_fn, retrive_fn)


# noinspection PyProtectedMember
def mongodb_config(
        *,
        connection_uri: str = None,
        client: pymongo.MongoClient = None,
        database: [str, pymongo.database.Database] = None,
        host=None,
        port=None,
        document_class=dict,
        tz_aware=None,
        connect=None,
        type_registry=None,
):
    """Single time config for MongoDb to set up a particular client, database etc. for all database models,
    avoiding repeat decorators etc.  This must be called before any class definitions subclassing MongoDbModel.

    The following code is equivalent:
    Snippet 1:
        @database('MyDB')
        class FirstModel(MongoDbModel):
            pass

        @database('MyDB')
        class FirstModel(MongoDbMOdel):
            pass

    Snippet 2:
        mongodb_config(database='MyDB')

        class FirstModel(MongoDbModel):
            pass

        class FirstModel(MongoDbMOdel):
            pass
    """
    # set the default client, and default database on the MongoDbModel class, NOT on subclasses directly
    if client:
        MongoDbModel._Defaults.CLIENT = client
    elif connection_uri:
        MongoDbModel._Defaults.CLIENT = pymongo.MongoClient(connection_uri, tz_aware=tz_aware, connect=connect,
                                                           type_registry=type_registry)
    elif (
            any(kwarg is not None for kwarg in [host, port, tz_aware, connect, type_registry]) or
            document_class is not dict
    ):
        client = pymongo.MongoClient(host, port, document_class, tz_aware, connect, type_registry)
        MongoDbModel._Defaults.CLIENT = client

    if isinstance(database, str):
        MongoDbModel._Defaults.DATABASE_NAME = database
    elif isinstance(database, pymongo.database.Database):
        MongoDbModel._Defaults.DATABASE_NAME = database.name


class MongoDbModel(DbModel):
    # MongoDbModel Default attributes
    class _Defaults:
        CLIENT: pymongo.MongoClient = None
        DATABASE_NAME: str = pathlib.Path(os.getcwd()).name
        SERIALIZER: Serializer = Serializer()

    # Subclass attributes (set in __init_subclass__)
    _CLIENT: Optional[pymongo.MongoClient]
    _DATABASE: Optional[pymongo.database.Database]
    _DATABASE_NAME: Optional[str]
    _COLLECTION: Optional[pymongo.database.Collection]
    _COLLECTION_NAME: Optional[str]
    _SERIALIZER: Optional[Serializer]
    _WEAKREFS: dict[bson.ObjectId, weakref.ref]
    _UNIQUE_FIELDS: list[str]
    _KEY_FIELD: str = '_id'

    # Instance attributes (set in __init__)
    _id: bson.ObjectId

    def __init__(self, *args, **kwargs):
        self.__class__.lazy_init_subclass()
        # initialize with default values where specified, None otherwise
        for key in self.__annotations__:
            default = self.__class__.__dict__.get(key)
            if isinstance(default, Callable):
                default = default()
            self.__dict__[key] = default

        values = {k: v for k, v in zip(self.__annotations__, args)}
        values.update(kwargs)
        self.__dict__.update(values)
        self.__class__._WEAKREFS[self._id] = weakref.ref(self)

    def __init_subclass__(cls, **kwargs):
        cls._SUBCLASS_INITIALIZED = False
        cls._CLIENT = None
        cls._DATABASE = None
        cls._DATABASE_NAME = None
        cls._COLLECTION = None
        cls._COLLECTION_NAME = None
        cls._SERIALIZER = None
        cls._WEAKREFS = {}
        cls._UNIQUE_FIELDS = []

        for anno, val in cls.__annotations__.items():
            if hasattr(val, '__origin__') and val.__origin__ is Key:
                if cls._KEY_FIELD != '_id':
                    raise MultipleKeys(f'Too many Key fields in model "{cls.__name__}". Use Unique'
                                       f' for multiple unique fields.')
                cls._KEY_FIELD = anno
                cls._UNIQUE_FIELDS.append(anno)
            if hasattr(val, '__origin__') and val.__origin__ is Unique:
                cls._UNIQUE_FIELDS.append(anno)
        cls.__init__.__signature__ = inspect.Signature(
            parameters=[inspect.Parameter('self', inspect.Parameter.POSITIONAL_ONLY, annotation=cls)] + [
                inspect.Parameter(k, inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=v)
                for k, v in cls.__annotations__.items()
            ],
            return_annotation=None,
        )
        register_type(cls, cls._db_store_, cls._db_retrieve_)

    @classmethod
    def lazy_init_subclass(cls) -> None:
        if not cls._SUBCLASS_INITIALIZED:
            if cls._CLIENT is None:
                if cls._Defaults.CLIENT is None:
                    cls._Defaults.CLIENT = pymongo.MongoClient()
                cls._CLIENT = cls._Defaults.CLIENT
            if cls._DATABASE is None:
                if cls._DATABASE_NAME:
                    cls._DATABASE = cls._CLIENT.get_database(cls._DATABASE_NAME)
                else:
                    cls._DATABASE = cls._CLIENT.get_database(cls._Defaults.DATABASE_NAME)
            if cls._COLLECTION is None:
                if not cls._COLLECTION_NAME:
                    cls._COLLECTION_NAME = cls.__name__
                cls._COLLECTION = cls._DATABASE.get_collection(cls._COLLECTION_NAME)
                for unique_field in cls._UNIQUE_FIELDS:
                    cls._COLLECTION.create_index(unique_field, unique=True)
                cls._COLLECTION_INITIALIZED = True
            if cls._SERIALIZER is None:
                cls._SERIALIZER = cls._Defaults.SERIALIZER
            cls._SUBCLASS_INITIALIZED = True

    @classmethod
    def register_type(cls, type_, store_fn, retrive_fn):
        if cls is MongoDbModel:
            cls._Defaults.SERIALIZER.register_type(type_, store_fn, retrive_fn)
        else:
            if cls._SERIALIZER is None:
                cls._SERIALIZER = cls._Defaults.SERIALIZER
            cls._SERIALIZER.register_type(type_, store_fn, retrive_fn)

    @classmethod
    def set_database(cls, database: [str, pymongo.database.Database]):
        if isinstance(database, pymongo.database.Database):
            cls._DATABASE = database
            return
        if isinstance(database, str):
            cls._DATABASE_NAME = database
            return
        raise NoDatabase(f'Unable to set database for {cls}')

    @classmethod
    def get_database(cls):
        return cls._DATABASE

    @classmethod
    def _set_client(cls, client: [str, pymongo.MongoClient]):
        cls._CLIENT = client

    @classmethod
    def _get_client(cls):
        return cls._CLIENT

    @classmethod
    def set_collection(cls, collection: [str, pymongo.database.Collection]):
        if isinstance(collection, pymongo.database.Collection):
            cls._COLLECTION = collection
            return
        elif isinstance(collection, str):
            if (database := cls.get_database()) is not None:
                cls._COLLECTION = database.get_collection(collection)
                return
        raise NoDatabase(f'Unable to set collection to {collection} for {cls} as there is no specified database')

    @classmethod
    def _init_collection(cls, collection: pymongo.database.Collection):
        for k in cls.__annotations__:
            if cls._get_field(k).unique_or_key:
                collection.create_index(k, unique=True)
        cls._COLLECTION_INITIALIZED = True

    @classmethod
    def get_collection(cls):
        collection = None
        if cls._COLLECTION is not None:
            collection = cls._COLLECTION
        database = cls.get_database()
        if database is not None:
            collection = database.get_collection(cls.__name__)
        if collection is None:
            raise NoCollection(f'{cls} has no specified collection, or database for '
                               f'generic collection')
        if not cls._COLLECTION_INITIALIZED:
            cls._init_collection(collection)
        return collection

    @classmethod
    def _get(cls, doc: dict):
        bson_id = doc['_id']
        if bson_id in cls._WEAKREFS:
            if obj := cls._WEAKREFS[bson_id]():
                # ensure the object isn't duplicated in memory, and uses any already existing one
                # this also ensures all references to the same db doc point to the same object
                return obj
        doc.update(cls._get_retrieve_vals(doc))
        return cls(**doc, ___internal___=True)

    @classmethod
    def _get_all_args(cls, *args, **kwargs):
        all_args = {k: v for k, v in zip(cls.__annotations__, args)}
        all_args.update(kwargs)
        return all_args

    @classmethod
    def query(cls, query) -> list[Self]:
        cls.lazy_init_subclass()
        return [cls._get(doc) for doc in cls.get_collection().find(query)]

    @classmethod
    def find(cls, *args, **kwargs) -> list[Self]:
        cls.lazy_init_subclass()
        all_args = cls._get_all_args(*args, **kwargs)
        return [cls._get(doc) for doc in cls.get_collection().find(cls._get_store_vals(all_args))]

    @classmethod
    def find_one(cls, *args, **kwargs) -> Optional[Self]:
        cls.lazy_init_subclass()
        all_args = cls._get_all_args(*args, **kwargs)
        if doc := cls.get_collection().find_one(cls._get_store_vals(all_args)):
            return cls._get(doc)

    @classmethod
    def delete_all(cls, *args, **kwargs):
        cls.lazy_init_subclass()
        all_args = cls._get_all_args(*args, **kwargs)
        cls.get_collection().delete_many(cls._get_store_vals(all_args))

    @classmethod
    def new(cls, *args, **kwargs):
        cls.lazy_init_subclass()
        all_args = cls._get_all_args(*args, **kwargs)
        doc = {k: all_args[k] if k in all_args else cls._get_default(k) for k in cls.__annotations__}
        try:
            insert_result = cls.get_collection().insert_one(cls._get_store_vals(doc))
        except pymongo.errors.DuplicateKeyError as e:
            raise UniqueConflict from e
        doc['_id'] = insert_result.inserted_id
        return cls(**doc, ___internal___=True)

    @classmethod
    def get_or_create(cls, *args, **kwargs):
        cls.lazy_init_subclass()
        return cls.find_one(*args, **kwargs) or cls(*args, **kwargs)

    @classmethod
    def _get_store_vals(cls, d: dict) -> dict:
        """Convert values in param d to database-storable values using cls._SERIALIZER

        :param d: dict containing raw values
        :return: dict containing database-storable values
        """
        return {k: cls._SERIALIZER.to_dict(v) for k, v in d.items()}

    @classmethod
    def _get_retrieve_vals(cls, d: dict) -> dict:
        """Convert values in param d from database-storable values back to their original values using cls._SERIALIZER
        :param d: dict containing database-storable values
        :return: dict containing raw values
        """
        rv = {}
        for k, v in d.items():
            if k in cls.__annotations__:
                rv[k] = cls._SERIALIZER.from_dict(cls.__annotations__[k], v)
            else:
                rv[k] = v
        return rv

    def update(self, **kwargs):
        """Update in-memory model instance with values in kwargs, and also write ONLY those changes to the database
        Behaviour differs from save method in that save also writes other changes:

        my_inst.field1 = 'not changed'
        my_inst.update(field2='changed too')  # ONLY writes field2 change to the database

        my_inst.field1 = 'not changed'
        my_inst.save(field2='changed too')  # Writes BOTH field1 and field2 change to the database
        """
        self.lazy_init_subclass()
        updates = {k: v for k, v in kwargs.items() if k in self.__annotations__}
        if updates:
            self.__dict__.update(updates)
            try:
                self.get_collection().update_one({'_id': self._id},
                                                 {'$set': self.__class__._get_store_vals(updates)})
            except pymongo.errors.DuplicateKeyError as e:
                raise UniqueConflict from e

    def delete(self):
        self.lazy_init_subclass()
        self.get_collection().delete_one({'_id': self._id})
        self._WEAKREFS.pop(self._id)

    def _db_store_(self):
        return getattr(self, self.__class__._KEY_FIELD)

    @classmethod
    def _db_retrieve_(cls, stored_val):
        return cls.find_one(**{cls._KEY_FIELD: stored_val})
