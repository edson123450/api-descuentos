import boto3 #import boto3
from boto3.dynamodb.conditions import Key #import boto3 conditions

def lambda_handler(event,context):
    # Entrada json
    partition_key=event['body']['tenant_id#c_estudiante']
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

