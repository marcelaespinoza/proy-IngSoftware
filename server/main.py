from fastapi import FastAPI
from database.db import create_tables
from routes.member import routes_member
from routes.emotion_log import routes_emotion_log

app = FastAPI()

app.include_router(routes_member, prefix="/member")
app.include_router(routes_emotion_log, prefix="/emotion_log")

create_tables()