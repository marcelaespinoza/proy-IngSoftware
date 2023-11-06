from controllers.emotion_ctlr import get_emotions, get_emotion_predominant
from fastapi import APIRouter
from typing import Optional

routes_emotion = APIRouter()

@routes_emotion.get('/all')
def get_all() -> Optional[dict]:  
    return get_emotions()

@routes_emotion.get('/predominant')
def get_predominant() -> Optional[dict]:  
    return get_emotion_predominant()