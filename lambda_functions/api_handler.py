import json
import boto3
import os

# Get table name from SSM Parameter Store
ssm = boto3.client('ssm')
dynamodb = boto3.resource('dynamodb')

def get_table():
    param = ssm.get_parameter(Name='/config/dynamoTableName')
    table_name = param['Parameter']['Value']
    return dynamodb.Table(table_name)

def handle_get(event):
    table = get_table()
    item_id = event['queryStringParameters'].get('id')
    response = table.get_item(Key={'id': item_id})
    
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Item not found'})
        }

def handle_post(event):
    import requests  # Make sure `requests` is included in deployment package if needed
    table = get_table()
    
    body = json.loads(event['body'])
    eks_url = os.environ.get('EKS_MICROSERVICE_URL')  # Set this via Lambda environment variable

    # Forward to EKS microservice
    eks_response = requests.post(eks_url, json=body)
    eks_data = eks_response.json()

    # Save to DynamoDB
    item_id = eks_data.get('id') or body.get('id') or 'generated-id'
    item = {'id': item_id, 'data': eks_data}
    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data stored successfully', 'data': eks_data})
    }

def main(event, context):
    method = event.get('httpMethod')
    
    if method == 'GET':
        return handle_get(event)
    elif method == 'POST':
        return handle_post(event)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        }