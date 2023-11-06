from controllers.emotion_log_ctlr import get_emotion_logs
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from database.db import dynamodb
from collections import Counter
from datetime import datetime
from typing import Optional

table = dynamodb.Table('Emotion')

def get_emotions() -> Optional[dict]:
    try:
        response: dict = dynamodb.scan(
            TableName=table
        )

        emotions: dict = {}
        for item in response['Items']:
            name: str = item.get('name', {}).get('S', ''),
            score: int = int(item.get('score', {}).get('N', '')),
            emotions[name] = score
        
        return emotions   
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)


def get_emotion_predominant() -> Optional[dict]:
    start_date: str = datetime(2023, 8, 28).strftime('%Y-%m-%d')
    end_date: str = datetime.now().strftime('%Y-%m-%d')

    try:
        items: dict = get_emotion_logs(start_date, end_date)
        emotions: list = [item['emotion']['S'] for item in items]
        emotion_counter: Counter = Counter(emotions)
        emotion_predominant: str = emotion_counter.most_common(1)[0][0]
        
        return {
            'emotion': emotion_predominant
        }
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)