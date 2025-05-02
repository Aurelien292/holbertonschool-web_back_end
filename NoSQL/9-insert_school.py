#!/usr/bin/env python3

"""
    Inserts a new document into a MongoDB collection.
    """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: The document fields and values.

    Returns:
        The _id of the inserted document.
    """
    object = mongo_collection.insert_one(kwargs)
    return object.inserted_id
