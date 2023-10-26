from fastapi import FastAPI
from database.db import create_tables
from routes.member import routes_member

app = FastAPI()

app.include_router(routes_member, prefix="/member")

create_tables()