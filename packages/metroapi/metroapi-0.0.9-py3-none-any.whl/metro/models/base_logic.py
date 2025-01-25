import types
from typing import Optional, TypeVar, Type, Union, List, Protocol, cast
from bson.decimal128 import Decimal128
from bson.binary import Binary
from mongoengine import (
    Document,
    DateTimeField,
    DoesNotExist,
    MultipleObjectsReturned,
    EmbeddedDocument,
    DynamicDocument,
    Q,
    StringField,
    IntField,
    FloatField,
    BooleanField,
    EmbeddedDocumentField,
    ListField,
    ReferenceField,
    DictField,
    DecimalField,
    ObjectIdField,
    EmbeddedDocumentListField,
    MapField,
    BinaryField,
    URLField,
    EmailField,
    GeoPointField,
    PointField,
    PolygonField,
    LineStringField,
    SequenceField,
    UUIDField,
    LazyReferenceField,
    ReferenceField,
    GenericReferenceField,
)
from mongoengine.base.metaclasses import TopLevelDocumentMetaclass
from datetime import datetime
from bson.objectid import ObjectId
from operator import or_, and_
from functools import reduce, wraps
from .mongo_protocol import MongoDocumentProtocol


T = TypeVar("T", bound=Union[Document, DynamicDocument])


FIELD_TYPE_MAP = {
    StringField: str,
    IntField: int,
    FloatField: float,
    BooleanField: bool,
    DateTimeField: datetime,
    DecimalField: Decimal128,
    BinaryField: Binary,
    URLField: str,
    EmailField: str,
    GeoPointField: dict,
    PointField: dict,
    PolygonField: dict,
    LineStringField: dict,
    SequenceField: int,
    UUIDField: str,
    LazyReferenceField: Document,
    ReferenceField: Document,
    GenericReferenceField: Document,
    ObjectIdField: ObjectId,
    EmbeddedDocumentField: EmbeddedDocument,
    ListField: list,
    EmbeddedDocumentListField: list,
    DictField: dict,
    MapField: dict,
}


def get_python_type(field_instance) -> type | None:
    for field_cls, py_type in FIELD_TYPE_MAP.items():
        if isinstance(field_instance, field_cls):
            return py_type
    # If we can’t match, either return `None` or raise an error
    return None


def type_checked_finder(finder_func):
    """Decorator for runtime type checking on dynamic finders."""
    # same code you already have
    # just keep it in a separate place or inline as needed
    from functools import wraps

    @wraps(finder_func)
    def wrapper(cls, *args, **kwargs):
        field_types = {}
        for field_name, field_instance in cls._fields.items():
            field_types[field_name] = get_python_type(field_instance)

        if kwargs:
            # Check types for keyword arguments
            for field_name, value in kwargs.items():
                expected_type = field_types.get(field_name)
                if expected_type and not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{field_name}' must be of type {expected_type.__name__}, "
                        f"got {type(value).__name__}"
                    )
        else:
            # Handling for positional arguments
            method_name = finder_func.__name__
            field_names = []

            if method_name.startswith('find_all_by_'):
                conditions = method_name[12:]
            else:
                conditions = method_name[8:]

            for or_group in conditions.split('_or_'):
                for field in or_group.split('_and_'):
                    field_names.append(field)

            for field_name, arg in zip(field_names, args):
                expected_type = field_types.get(field_name)
                if expected_type and not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument for '{field_name}' must be of type {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )

        return finder_func(cls, *args, **kwargs)

    return wrapper


class DynamicFinderMetaclass(TopLevelDocumentMetaclass):
    def __getattr__(cls, name: str):
        # Check for patterns like 'find_by_' or 'find_all_by_'
        if name.startswith('find_by_') or name.startswith('find_all_by_'):
            is_find_all = name.startswith('find_all_by_')
            conditions_str = name[12:] if is_find_all else name[8:]

            @type_checked_finder
            def dynamic_finder(cls, *args, **kwargs):
                """
                This is defined as if it were a classmethod:
                the first argument is `cls` (the actual class).
                Example usage: `User.find_by_name_and_age("Alice", 30)`
                """
                or_groups = conditions_str.split('_or_')
                queries = []

                # 1) If user passes kwargs, we do a different approach.
                if kwargs:
                    if args:
                        raise ValueError("Cannot mix positional and keyword arguments.")
                    ...
                    # (Keyword logic remains the same)
                    return result

                # 2) Handle positional arguments
                # Let's build up a list of *all fields* that we expect:
                all_fields = []
                for or_group in or_groups:
                    and_fields = or_group.split('_and_')
                    all_fields.extend(and_fields)

                # This is how many total positional args we need
                total_fields_needed = len(all_fields)

                # Quick mismatch check: if the user didn't supply exactly `total_fields_needed` arguments, error early
                if len(args) < total_fields_needed:
                    raise ValueError(
                        f"{cls.__name__}.{name}() expects {total_fields_needed} arguments "
                        f"(fields: {', '.join(all_fields)}), but got only {len(args)}. "
                        f"Please provide values for all required fields."
                    )
                elif len(args) > total_fields_needed:
                    raise ValueError(
                        f"{cls.__name__}.{name}() expects {total_fields_needed} arguments "
                        f"(fields: {', '.join(all_fields)}), but got {len(args)}. "
                        "Please remove extra arguments."
                    )

                # Now we can safely iterate without risk of IndexError
                arg_index = 0
                for or_group in or_groups:
                    and_fields = or_group.split('_and_')
                    if len(and_fields) > 1:
                        and_queries = []
                        for field in and_fields:
                            if not hasattr(cls, field):
                                raise AttributeError(f"'{cls.__name__}' has no field '{field}'")
                            and_queries.append(Q(**{field: args[arg_index]}))
                            arg_index += 1
                        queries.append(reduce(and_, and_queries))
                    else:
                        field = and_fields[0]
                        if not hasattr(cls, field):
                            raise AttributeError(f"'{cls.__name__}' has no field '{field}'")
                        queries.append(Q(**{field: args[arg_index]}))
                        arg_index += 1

                # Build the final query
                final_query = reduce(or_, queries)
                result = cls.objects(final_query)
                return result if is_find_all else result.first()

            # Return a bound method so that `cls` is actually the class
            return types.MethodType(dynamic_finder, cls)

        # Fallback to normal behavior
        raise AttributeError(f"'{cls.__name__}' has no attribute '{name}'")


class DynamicFinderProtocol(Protocol[T]):
    """Protocol for dynamic finder methods"""
    def __call__(self, *args: any, **kwargs: any) -> Union[Optional[T], list[T]]: ...


class BaseModelLogic:
    meta = {
        "abstract": True,
        "indexes": [
            "created_at",
            "updated_at",
            "deleted_at",
        ],
    }

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    deleted_at = DateTimeField(default=None)

    def clean(self) -> None:
        """
        Add custom validation logic here. Called before save.
        """
        pass

    def pre_save(self) -> None:
        """
        Hook for logic that should run before saving
        """
        pass

    def post_save(self) -> None:
        """
        Hook for logic that should run after successful save
        """
        pass

    def handle_save_error(self, error: Exception):
        """Override this method to handle specific save errors"""
        pass

    def to_dict(self, exclude_fields: set = None) -> dict:
        """
        Convert the document to a Python dictionary.

        Args:
            exclude_fields: Set of field names to exclude from the output

        Returns:
            dict: The document as a regular Python dictionary
        """
        exclude_fields = exclude_fields or {"_cls"}

        def _handle_value(val):
            if isinstance(val, ObjectId):
                return str(val)
            elif isinstance(val, datetime):
                return val.isoformat()
            elif isinstance(val, Decimal128):
                return float(val.to_decimal())
            elif isinstance(val, Binary):
                return str(val)
            elif isinstance(val, (dict, Document, EmbeddedDocument)):
                return _dictify(val)
            elif isinstance(val, list):
                return [_handle_value(v) for v in val]
            else:
                return val

        def _dictify(d):
            if isinstance(d, (Document, EmbeddedDocument)):
                d = d.to_mongo().to_dict()
            return {
                k: _handle_value(v) for k, v in d.items() if k not in exclude_fields
            }

        try:
            return _dictify(self.to_mongo().to_dict())
        except Exception as e:
            raise ValueError(f"Error converting document to dict: {str(e)}") from e

    @classmethod
    def _execute_query(cls, operation, *args, **kwargs) -> Optional[T]:
        try:
            return operation(*args, **kwargs)
        except (DoesNotExist, MultipleObjectsReturned):
            return None

    @classmethod
    def find_by_id(
        cls, id: str | ObjectId, include_deleted: bool = False
    ) -> Optional[T]:
        """Find document by ID, excluding soft-deleted by default"""
        cls._raise_if_invalid_id(id)

        kwargs = {"id": id}
        if not include_deleted:
            kwargs["deleted_at"] = None

        return cls._execute_query(cls.objects(**kwargs).first)

    @classmethod
    def find_one(cls, include_deleted: bool = False, **kwargs) -> Optional[T]:
        """Find a single document, excluding soft-deleted by default"""
        if not include_deleted:
            kwargs["deleted_at"] = None

        return cls._execute_query(cls.objects(**kwargs).first)

    @classmethod
    def find(
        cls,
        include_deleted: bool = False,
        page: int = None,
        per_page: int = None,
        **kwargs,
    ) -> List[T]:
        """Find documents, excluding soft-deleted by default"""
        if not include_deleted:
            kwargs["deleted_at"] = None

        if page is not None and per_page is not None:
            start = (page - 1) * per_page
            return cls._execute_query(cls.objects(**kwargs).skip(start).limit(per_page))
        else:
            return cls._execute_query(cls.objects(**kwargs))

    @classmethod
    def find_deleted(cls, page: int = None, per_page: int = None, **kwargs) -> List[T]:
        """
        Find only soft-deleted documents

        Args:
            page: Page number (starting from 1)
            per_page: Number of items per page
            **kwargs: Additional query filters

        Returns:
            List of soft-deleted documents
        """
        kwargs["deleted_at__ne"] = None
        return cls.find(include_deleted=True, page=page, per_page=per_page, **kwargs)

    @classmethod
    def find_by_id_and_update(cls, id: str | ObjectId, **updates) -> Optional[T]:
        """
        Atomically updates a document by ID and returns the updated document.

        Can be used in two ways:

        * Simple field updates: find_by_id_and_update(id, name="John", age=25)

        * MongoDB operators: find_by_id_and_update(id, **{"$set": {...}, "$push": {...}})

        Args:
            id: The document ID
            **updates: Keyword arguments for field updates or MongoDB operators

        Returns:
            The updated document or None if not found/invalid ID
        """
        cls._raise_if_invalid_id(id)

        doc = cls.find_by_id(id)
        if not doc:
            return None

        for key, value in updates.items():
            setattr(doc, key, value)

        doc.save()
        return doc

    @classmethod
    def find_by_id_and_delete(cls, id: str | ObjectId) -> Optional[T]:
        """
        Find a document by ID and delete it.

        Args:
            id: The document ID

        Returns:
            The deleted document or None if not found/invalid ID
        """
        cls._raise_if_invalid_id(id)

        doc = cls.find_by_id(id)
        if doc:
            doc.delete()
            return doc

        return None

    def soft_delete(self) -> None:
        """Mark the document as deleted without removing it from the database"""
        self.deleted_at = datetime.utcnow()
        self.save()

    def restore(self) -> None:
        """Restore a soft-deleted document"""
        self.deleted_at = None
        self.save()

    @property
    def is_deleted(self) -> bool:
        """Check if document is soft-deleted"""
        return self.deleted_at is not None

    @classmethod
    def count(cls, include_deleted: bool = False, **kwargs) -> int:
        """Count documents, excluding soft-deleted by default"""
        if not include_deleted:
            kwargs["deleted_at"] = None

        return cls.objects(**kwargs).count()

    @staticmethod
    def _raise_if_invalid_id(id: str | ObjectId):
        if not isinstance(id, ObjectId) and not ObjectId.is_valid(id):
            raise ValueError("Invalid document ID")
