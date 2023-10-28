from boto3 import resource
from os import getenv

dynamodb = resource('dynamodb',
         aws_access_key_id=getenv("aws_access_key_id"),
         aws_secret_access_key=getenv("aws_secret_access_key"),
         aws_session_token=getenv("aws_session_token"),
         region_name=getenv("aws_region_name"))

tables = [
    {
        "TableName": "Member",
        "KeySchema": [
            {
                'AttributeName': 'code',
                'KeyType': 'HASH'
            }
        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'code',
                'AttributeType': 'S'
            }
        ],
        "GlobalSecondaryIndexes": []
    },
    {
        "TableName": "EmotionLog",
        "KeySchema": [
            {
                "AttributeName": "member_code",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "timestamp",
                "KeyType": "RANGE"
            }
        ],
        "AttributeDefinitions": [
            {
                "AttributeName": "member_code",
                "AttributeType": "S"
            },
            {
                "AttributeName": "timestamp",
                "AttributeType": "S"
            }
        ],
        "GlobalSecondaryIndexes": [
            {
                "IndexName": "TimestampIndex",
                "KeySchema": [
                    {
                        "AttributeName": "timestamp",
                        "KeyType": "HASH"
                    }
                ],
                "Projection": {
                    "ProjectionType": "ALL"
                }
            }
        ]
    }
]

def create_tables():
    try:
        for table in tables:
            if table["GlobalSecondaryIndexes"] == []: 
                dynamodb.create_table(
                    TableName=table["TableName"],
                    KeySchema=table["KeySchema"],
                    AttributeDefinitions=table["AttributeDefinitions"],
                    BillingMode="PAY_PER_REQUEST"
                )
            else:
                dynamodb.create_table(
                    TableName=table["TableName"],
                    KeySchema=table["KeySchema"],
                    AttributeDefinitions=table["AttributeDefinitions"],
                    GlobalSecondaryIndexes=table["GlobalSecondaryIndexes"],
                    BillingMode="PAY_PER_REQUEST"
                )
    except Exception as e:
        print(e)