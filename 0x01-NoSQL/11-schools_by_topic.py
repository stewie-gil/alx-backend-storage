#!/usr/bin/env python3
"""module contains the schools_by_topic function""" 

def schools_by_topic(mongo_collection, topic):
    """Return the list of schools having a specific topic"""
    query = {"topics": topic}
    schools = mongo_collection.find(query)
    return schools
