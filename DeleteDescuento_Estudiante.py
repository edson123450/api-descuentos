import boto3
import json

def lambda_handler(event,context):
    partition_key=event['body']['tenant_id#c_estudiante']
    sort_key=event['body']['c_descuento']

    # Inicio - Proteger el Lambda
    token = event['headers']['Authorization']
    lambda_client = boto3.client('lambda')
    payload_string = '{ "token": "' + token + '" }'
    invoke_response = lambda_client.invoke(
        FunctionName="ValidarTokenEstudiante",
        InvocationType='RequestResponse',
        Payload=payload_string
    )
    response = json.loads(invoke_response['Payload'].read())
    print(response)
    if response['statusCode'] == 403:
        return {
            'statusCode': 403,
            'status': 'Forbidden - Acceso no autorizado'
        }
    # Fin - Proteger el Lambda

    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('tabla_descuentos')
    response=table.delete_item(
        Key={
            'tenant_id#c_estudiante': partition_key,
            'c_descuento': sort_key
        }
    )

    return {
        'statusCode': 200,
        'response':response
    }
