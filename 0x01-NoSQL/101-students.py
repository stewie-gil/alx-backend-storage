#!/usr/bin/env python3
"""This module contains top students function"""


def top_students(mongo_collection):
    """Return all students sorted by average score"""
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]
    
    students = list(mongo_collection.aggregate(pipeline))
    return students
