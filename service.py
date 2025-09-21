from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    name: str = raw_data.name
    username: str = raw_data.username

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {"id": id, "name": name, "username": username}.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_tasks(db: Session):

    query = db.query(models.Tasks)

    tasks_all = query.all()
    tasks_all = (
        [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tasks_all": tasks_all},
    }
    return res


async def get_tasks_id(db: Session, id: int):

    query = db.query(models.Tasks)
    query = query.filter(and_(models.Tasks.id == id))

    tasks_one = query.first()

    tasks_one = (
        (tasks_one.to_dict() if hasattr(tasks_one, "to_dict") else vars(tasks_one))
        if tasks_one
        else tasks_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tasks_one": tasks_one},
    }
    return res


async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    description: str = raw_data.description
    is_completed: int = raw_data.is_completed
    due_date: datetime.date = raw_data.due_date
    user_id: int = raw_data.user_id

    record_to_be_added = {
        "user_id": user_id,
        "due_date": due_date,
        "description": description,
        "is_completed": is_completed,
    }
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tasks_inserted_record": tasks_inserted_record},
    }
    return res


async def put_tasks_id(db: Session, raw_data: schemas.PutTasksId):
    id: int = raw_data.id
    description: str = raw_data.description
    is_completed: int = raw_data.is_completed
    due_date: datetime.date = raw_data.due_date
    user_id: int = raw_data.user_id

    query = db.query(models.Tasks)
    query = query.filter(and_(models.Tasks.id == id))
    tasks_edited_record = query.first()

    if tasks_edited_record:
        for key, value in {
            "id": id,
            "user_id": user_id,
            "due_date": due_date,
            "description": description,
            "is_completed": is_completed,
        }.items():
            setattr(tasks_edited_record, key, value)

        db.commit()
        db.refresh(tasks_edited_record)

        tasks_edited_record = (
            tasks_edited_record.to_dict()
            if hasattr(tasks_edited_record, "to_dict")
            else vars(tasks_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tasks_edited_record": tasks_edited_record},
    }
    return res


async def delete_tasks_id(db: Session, id: int):

    query = db.query(models.Tasks)
    query = query.filter(and_(models.Tasks.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict()
    else:
        tasks_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"tasks_deleted": tasks_deleted},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    name: str = raw_data.name
    username: str = raw_data.username

    record_to_be_added = {"name": name, "username": username}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res
