from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from member_ctlr import get_member
from database.db import dynamodb
from typing import Optional
import ast

table = dynamodb.Table('PsychologistSchedule')

def get_psychologist_schedules_details() -> Optional[dict]:
    try:
        response: dict = dynamodb.scan(
            TableName=table
        )

        schedules: dict = {}
        for item in response['Items']:
            code: str = item.get('member_coe', {}).get('S')
            value: str = item.get('schedule', {}).get('S', '').replace("'", "\"")
            data: list = ast.literal_eval(value) 
            schedule: dict = { item['day']: item['hours'] for item in data }
            days: list = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
            for day in days:
                schedule.setdefault(day, [])
            schedules[code] = schedule

        for code in schedules.keys():
            member: dict = get_member(code)
            schedules[code]['name'] = member['name']
            schedules[code]['email'] = member['email']

        return schedules 
    except ClientError as e:
        return JSONResponse(content=e.response['Error'], status_code=500)