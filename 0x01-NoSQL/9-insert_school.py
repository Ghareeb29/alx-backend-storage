#!/usr/bin/env python3
"""
Module for Python function which
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.

    Args:
    mongo_collection: A pymongo collection object
    **kwargs: Keyword arguments representing
    the fields and values of the document to insert

    Returns:
    The _id of the newly inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
