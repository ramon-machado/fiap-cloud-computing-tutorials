import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO


dao = BaseDAO('eventos-pizzaria')

def detailHandlerpizza(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True
    
def sourceHandlerpizza(event, context):
    dao.put_item(
        {'pedido':(format(json.dumps(event['detail']['pedido']))),
        'status':(format(json.dumps(event['detail']['status']))),
        'cliente':(format(json.dumps(event['detail']['cliente']))),
        'time':(format(json.dumps(event['time'])))}
    
    )
