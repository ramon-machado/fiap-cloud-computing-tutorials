import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO


def detailHandlerpizza(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True
    
def sourceHandlerpizza(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True