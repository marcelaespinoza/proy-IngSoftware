from database.db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key
from collections import defaultdict
from typing import Optional

table = dynamodb.Table("EmotionLog")
emotion_scores = {
    'tristeza': 10,
    'estres': 4,
    'ansiedad': 5,
    'frustracion': 5,
    'enojo': 8,
    'aburrimiento': 2,
    'preocupacion': 3,
    'motivacion': -5,
    'felicidad': -10,
    'satisfaccion': -4,
    'alivio': -2
}


def get_emotion_logs_member(member_code: str, start_date: str, end_date: str) -> Optional[dict]:
    try:
        response = table.query(
            KeyConditionExpression=Key('member_code').eq(member_code) &
                                   Key('timestamp').between(f"{start_date}T00:00:00", f"{end_date}T23:59:59")
        )
        return response['Items']
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)


def get_emotion_logs(start_date: str, end_date: str) -> Optional[dict]:
    try:
        response: dict = table.query(
            KeyConditionExpression=Key('timestamp').between(f"{start_date}T00:00:00", f"{end_date}T23:59:59")
        )
        return response['Items']
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)


# Auxiliary Functions

def emotions_member_codes(items: dict) -> dict:
    emotions: defaultdict = defaultdict(list)
    for item in items:
        emotion: str = item['emotion']['S']
        code: str = item['member_code']['S']
        emotions[emotion].append(code)

    return dict(emotions) 
