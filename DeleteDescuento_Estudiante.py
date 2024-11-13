import boto3

def lambda_handler(event,context):
    partition_key=event['body']['tenant_id#c_estudiante']
    sort_key=event['body']['c_descuento']

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