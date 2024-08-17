#!/usr/bin/env python3
""" Module for log stats """
from pymongo import MongoClient


def log_stats():
    """Function for log stats"""
    # Connect to MongoDB
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    nginx = db.nginx

    # Get total number of logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Get counts for each method
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Get count of status checks
    status_check = nginx.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
