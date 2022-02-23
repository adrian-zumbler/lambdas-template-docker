"""Python AWS Lambda Hello World Example
   This example Lambda function will simply return 'Hello from Lambda!' and
   a HTTP Status Code 200.
"""
from pymongo import MongoClient
import json

def lambda_handler(event, context):
    for record in event['Records']:
        print("test")
        payload = record["body"]
        print(str(payload))