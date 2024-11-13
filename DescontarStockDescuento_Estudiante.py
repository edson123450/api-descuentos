import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event,context):
    partition_key=event['body']['tenant_id#c_estudiante']
    sort_key=event['body']['c_descuento']
    datos_descuento=['body']['datos_descuento']

    dynamodb=boto3.resource('dynamodb')
    table=dynamodb.Table('tabla_descuentos')
    response=table.update_item(
        Key={
            'tenant_id#c_estudiante':partition_key,
            'c_descuento':sort_key
        },
        UpdateExpression="set datos_descuento=:datos_descuento",
        ExpressionAtributeValues={
            ':datos_descuento': datos_descuento
        },
        ReturnValues="UPDATED_NEW"
    )
    return {
        'statusCode': 200,
        'response': response
    }
