from fastapi import APIRouter
from models.member import Member
from database.member import create_member, get_member, get_members, delete_member, update_member

routes_member = APIRouter()

@routes_member.post("/create", response_model=Member)
def create(member: Member):
    return create_member(member.model_dump())

@routes_member.get("/get/{code}")
def get_by_code(code: str):
    return get_member(code)

@routes_member.get("/all")
def get_all():
    return get_members()

@routes_member.delete("/delete")
def delete(member: Member):
    return delete_member(member.model_dump())

@routes_member.put("/update")
def update(member: Member):
    return update_member(member.model_dump())