import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO


dao = BaseDAO('eventos-pizzaria')

def detailHandlerpizza(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True
    
def sourceHandlerpizza(event, context):
    dao.put_item({'pedido':("pedido: {}".format(json.dumps(event)))})
    #dao.put_item("event: {}".format(json.dumps(event)))
    
    return True