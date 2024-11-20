import boto3 #import boto3
from boto3.dynamodb.conditions import Key #import boto3 conditions
import json

def lambda_handler(event,context):
    # Entrada json
    partition_key=event['body']['tenant_id#c_estudiante']

    # Inicio - Proteger el Lambda
    token=event['headers']['Authorization']
    lambda_client=boto3.client('lambda')
    payload_string='{ "token": "' +token+ '" }'
    invoke_response=lambda_client.invoke(
        FunctionName="ValidarTokenEstudiante",
        InvocationType='RequestResponse',
        Payload=payload_string
    )
    response=json.loads(invoke_response['Payload'].read())
    print(response)
    if response['statusCode']==403:
        return {
            'statusCode':403,
            'status': 'Forbidden - Acceso no autorizado'
        }
    # Fin - Proteger el Lambda

    # Proceso
    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('tabla_descuentos')
    response=table.query(
        KeyConditionExpression=Key('tenant_id#c_estudiante').eq(partition_key)
    )
    items=response['Items']
    num_reg=response['Count']
    # Salida json
    return {
        'statusCode':200,
        'tenant_id#c_estudiante':partition_key,
        'numero_tipoDescuentos':num_reg,
        'tipoDescuentos':items
    }
