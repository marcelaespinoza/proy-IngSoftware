from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("EmotionLog")
emotion_scores = {
    'tristeza': -10,
    'estres': -4,
    'ansiedad': -5,
    'frustracion': -5,
    'enojo': -8,
    'aburrimiento': -2,
    'preocupacion': -3,
    'motivacion': 5,
    'felicidad': 10,
    'satisfaccion': 4,
    'alivio': 2
}

def create_emotion_log(emotion_log: dict):
    try:
        table.put_item(Item=emotion_log)
        score = emotion_scores.get(emotion_log["emotion"], 0)
        dynamodb.update_item(
            TableName='Member',
            Key={'code': {'S': emotion_log["member_code"]}},
            UpdateExpression='SET emotion_score = emotion_score + :score',
            ExpressionAttributeValues={':score': {'N': str(score)}}
        )
        return emotion_log
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def get_emotion_logs_by_member(member_code: str, start_date: str, end_date: str):
    try:
        response = table.query(
            KeyConditionExpression=Key('member_code').eq(member_code) &
                                   Key('timestamp').between(f"{start_date}T00:00:00", f"{end_date}T23:59:59")
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def get_emotion_logs(start_date: str, end_date: str):
    try:
        response = table.query(
            IndexName='DateIndex',
            KeyConditionExpression=Key('timestamp').between(f"{start_date}T00:00:00", f"{end_date}T23:59:59")
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def delete_emotion_log(emotion_log: dict):
    try:
        response = table.delete_item(
            Key={
                "member_code": emotion_log["member_code"],
                "timestamp": emotion_log["timestamp"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def update_emotion_log(emotion_log: dict):
    try:
        response = table.put_item(
            Key={
                "member_code": emotion_log["member_code"],
                "timestamp": emotion_log["timestamp"]
            },
            UpdateExpression="SET emotion = :emotion",
            ExpressionAttributeValues={
                ":emotion": emotion_log["emotion"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)