import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
from sqsHandler import SqsHandler
from env import Variables


dao = BaseDAO('eventos-pizzaria')

def detailHandlerpizza(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    print(type(event))
    sqs.send("event: {}".format(json.dumps(event)))
        
def sourceHandlerpizza(event, context):
    dao.put_item(
        {'pedido':(format(json.dumps(event['detail']['pedido']))),
        'status':(format(json.dumps(event['detail']['status']))),
        'cliente':(format(json.dumps(event['detail']['cliente']))),
        'time':(format(json.dumps(event['time'])))}
    
    )
    
def consumerHandlerpizza(event, context):
    env = Variables()
    sqs = SqsHandler(env.get_sqs_url())
    while(True):
        response = sqs.getMessage(1)
        if(len(response) == 0):
            break
        print(response)