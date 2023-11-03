from fastapi import APIRouter
from models.emotion_log import EmotionLog
from database.emotion_log import create_emotion_log, get_emotion_logs, get_emotion_logs_by_member, delete_emotion_log, update_emotion_log

routes_emotion_log = APIRouter()

@routes_emotion_log.post("/create", response_model=EmotionLog)
def create(emotion_log: EmotionLog):
    print(emotion_log.model_dump())
    return create_emotion_log(emotion_log.model_dump())
    
@routes_emotion_log.get("/get/{member_code}/{start_date}/{end_date}")
def get_by_code(member_code: str, start_date: str, end_date: str):
    return get_emotion_logs_by_member(member_code, start_date, end_date)

@routes_emotion_log.get("/all/{start_date}/{end_date}")
def get_all(start_date: str, end_date: str):
    return get_emotion_logs(start_date, end_date)

@routes_emotion_log.delete("/delete")
def delete(emotion_log: EmotionLog):
    return delete_emotion_log(emotion_log.model_dump())

@routes_emotion_log.put("/update")
def update(emotion_log: EmotionLog):
    return update_emotion_log(emotion_log.model_dump())
