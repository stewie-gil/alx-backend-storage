#!/usr/bin/env python3
"""This module contains the log_stats method"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """Total number of logs"""
    total_logs = mongo_collection.count_documents({})

    print(f"{total_logs} logs")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"method {method}:", count)

    # Number of documents with method=GET and path=/status
    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    log_stats(collection)
