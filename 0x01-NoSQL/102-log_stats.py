#!/usr/bin/env python3
"""this module contains logstats module"""


from pymongo import MongoClient


def log_stats(mongo_collection):
    """ Total number of logs"""
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

    # Top 10 IPs
    top_ips_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips_result = mongo_collection.aggregate(top_ips_pipeline)
    print("IPs:")
    for ip_record in top_ips_result:
        print(f"    {ip_record['_id']}: {ip_record['count']}")

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    log_stats(collection)
