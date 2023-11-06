from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from database.db import dynamodb
from typing import Optional

table = dynamodb.Table('Area')

def get_areas() -> Optional[list]:
    areas: list = []

    try:
        response: dict = dynamodb.scan(
            TableName=table
        )
        for item in response['Items']:
            name: str = item.get('name', {}).get('S', '')
            areas.append(name)
        
        return areas   
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)