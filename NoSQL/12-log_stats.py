#!/usr/bin/env python3
""" Nginx log stats """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    collection = client.logs.nginx

    print("{} logs".format(collection.count()))

    print("Methods:")
    print("\tmethod GET: {}".format(collection.find({"method": "GET"}).count()))
    print("\tmethod POST: {}".format(collection.find({"method": "POST"}).count()))
    print("\tmethod PUT: {}".format(collection.find({"method": "PUT"}).count()))
    print("\tmethod PATCH: {}".format(collection.find({"method": "PATCH"}).count()))
    print("\tmethod DELETE: {}".format(collection.find({"method": "DELETE"}).count()))

    print("{} status check".format(
        collection.find({
            "method": "GET",
            "path": "/status"
        }).count()
    ))
