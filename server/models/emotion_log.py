from pydantic import BaseModel

class EmotionLog(BaseModel):
    member_code: str
    date: str
    hour: str
    emotion: str