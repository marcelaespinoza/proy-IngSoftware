from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from database.db import dynamodb
from typing import Optional

table = dynamodb.Table('Member')

def get_member(code: str) -> Optional[dict]:
    try:
        response: dict = dynamodb.get_item(
            TableName=table,
            Key={
                'tenant_id': {'S': 'UTEC'}, 
                'code': {'S': code}
            },
        )
        
        item: dict = response.get('Item', {})

        member: dict = {
            'code': item.get('code', {}).get('S', ''),
            'name': item.get('nombre', {}).get('S', ''),
            'area': item.get('area', {}).get('S', ''),
            'email': item.get('correo', {}).get('S', ''),
            'neg_score': int(item.get('neg_score', {}).get('N', '0'))
        }
        return member
        
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)


def update_member_state_score(code: str, state: int) -> Optional[dict]: 
    member: dict = get_member(code)
    current_score: int = int(member['neg_score'])
    new_score: int = calculate_new_score(current_score, state)

    try:    
        dynamodb.update_item(
            TableName=table,
            Key={
                'tenant_id': {'S': 'UTEC'}, 
                'code': {'S': code}
            },
            UpdateExpression='SET neg_score = :val1, state = :val2',
            ExpressionAttributeValues={
                ':val1': {'N': str(new_score)},
                ':val2': {'N': str(state)}
            }
        )

        return {
            'message': f'Updated score for member with code {code}. New score: {new_score})'
        }
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


def get_members_top_negative(limit: int) -> Optional[list]:
    members: list = []
    
    try:
        response: dict = dynamodb.scan(
            TableName=table,
            ProjectionExpression='code, name, area, neg_score, email', 
            ExpressionAttributeNames={'#neg_score': 'neg_score'}, 
            ExpressionAttributeValues={':val': {'N': '0'}},  
            FilterExpression='#neg_score >= :val',
        )
        
        items: dict = sorted(
            response['Items'], 
            key=lambda x: int(x['neg_score']['N']), 
            reverse=True
        )[:limit]
        
        for item in items:
            member: dict = {
                'code': item.get('code', {}).get('S', ''),
                'name': item.get('name', {}).get('S', ''),
                'area': item.get('area', {}).get('S', ''),
                'email': item.get('email', {}).get('S', ''),
                'neg_score': int(item.get('neg_score', {}).get('N', '0'))
            }
            members.append(member)

        return members
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)


# Auxiliary Functions

def calculate_new_score(current_score: int, state: int) -> int:
    return current_score - (20 if state == 1 else (50 if state == 2 else (100 if state == 3 else 0)))

convert_response: function = lambda response: {
    key: next(iter(value.values())) for key, value in response.get('Item', {}).items()
}