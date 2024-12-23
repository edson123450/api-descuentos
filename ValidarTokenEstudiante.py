import boto3
from datetime import datetime

def lambda_handler(event,context):
    token=event['token']

    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('tabla_tokens_acceso')

    response=table.get_item(
        Key={
            'token':token
        }
    )
    if 'Item' not in response:
        return {
            'statusCode':403,
            'body': 'Token no existe'
        }
    else:
        expires=response['Item']['expires']
        now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if now>expires:
            return {
                'statusCode':403,
                'body': 'Token expirado'
            }

    return {
        'statusCode': 200,
        'body': 'Token valido'
    }
