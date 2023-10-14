import json


def detailHandlerpizza(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True
    
def sourceHandlerpizza(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True