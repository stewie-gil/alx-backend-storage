#!/usr/bin/env python3
""" this module contains update_topics"""


def update_topics(mongo_collection, name, topics):
    """Update topics of a school document based on the name"""
    filter_criteria = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter_criteria, update)
