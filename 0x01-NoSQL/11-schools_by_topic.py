#!/usr/bin/env python3
"""
Module for Python function which
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
    mongo_collection: A pymongo collection object
    topic: (string) The topic to search for

    Returns:
    A list of school documents that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
