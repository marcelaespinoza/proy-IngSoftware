from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("Member")

def create_member(member: dict):
    try:
        table.put_item(Item=member)
        return member
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def get_member(code: str):
    try:
        response = table.query(
            KeyConditionExpression=Key("code").eq(code)
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def get_members():
    try:
        response = table.scan(
            Limit=20,
            AttributesToGet=["name", "code"]
        )
        return response["Items"]
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def delete_member(member: dict):
    try:
        response = table.delete_item(
            Key={
                "code": member["code"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)

def update_member(member: dict):
    try:
        response = table.update_item(
            Key={
                "code": member["code"]
            },
            UpdateExpression="SET name = :name, area = :area, age = :age, email = :email, role = :role, emotion_score = :emotion_score",
            ExpressionAttributeValues={
                ":name": member["name"],
                ":area": member["area"],
                ":age": member["age"],
                ":email": member["email"],
                ":role": member["role"],
                ":emotion_score": member["emotion_score"]
            }
        )
        return response
    except ClientError as e:
        return JSONResponse(content=e.response["Error"], status_code=500)