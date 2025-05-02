#!/usr/bin/env python3
'''
Stats about nginx logs stored in MongoDB
'''
from pymongo import MongoClient


def log_stats():
    x = MongoClient('mongodb://localhost:27017/').logs.nginx

    print(f'{x.count_documents({})} logs')
    print(f'Methods:')
    print(f'\tGET: {x.count_documents({"method": "GET"})}')
    print(f'\tPOST: {x.count_documents({"method": "POST"})}')
    print(f'\tPUT: {x.count_documents({"method": "PUT"})}')
    print(f'\tPATCH: {x.count_documents({"method": "PATCH"})}')
    print(f'\tDELETE: {x.count_documents({"method": "DELETE"})}')
    print(f'{x.count_documents({"method": "GET", "path": "/status"})} '
          'status check')


if __name__ == "__main__":
    log_stats()
