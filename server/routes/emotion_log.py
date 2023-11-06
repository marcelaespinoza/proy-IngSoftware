from controllers.emotion_log_ctlr import get_emotion_logs, get_emotion_logs_member 
from fastapi import APIRouter
from typing import Optional

routes_emotion_log = APIRouter()

@routes_emotion_log.get('/member_code/{member_code}/{start_date}/{end_date}')
def get_by_code(member_code: str, start_date: str, end_date: str) -> Optional[dict]:
    return get_emotion_logs_member(member_code, start_date, end_date)

@routes_emotion_log.get('/all/{start_date}/{end_date}')
def get_all(start_date: str, end_date: str) -> Optional[dict]:
    return get_emotion_logs(start_date, end_date)