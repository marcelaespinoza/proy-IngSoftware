from boto3 import resource
from os import getenv

dynamodb = resource('dynamodb',
         aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
         aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
         aws_session_token=getenv("AWS_SESSION_TOKEN"),
         region_name=getenv("AWS_REGION_NAME"))

tables = [
    {
        "TableName": "members",
        "KeySchema": [
            {
                'AttributeName': 'code',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'age',
                'KeyType': 'RANGE' 
            }
        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'code',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'age',
                'AttributeType': 'N'
            },
        ],
    },
]

def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)