from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    name: Optional[str]=None
    username: Optional[str]=None


class ReadUsers(BaseModel):
    name: Optional[str]=None
    username: Optional[str]=None
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    description: Optional[str]=None
    is_completed: Optional[int]=None
    due_date: Optional[datetime.date]=None
    user_id: Optional[int]=None


class ReadTasks(BaseModel):
    description: Optional[str]=None
    is_completed: Optional[int]=None
    due_date: Optional[datetime.date]=None
    user_id: Optional[int]=None
    class Config:
        from_attributes = True




class PutUsersId(BaseModel):
    id: Optional[int]=None
    name: Optional[str]=None
    username: Optional[str]=None

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    description: Optional[str]=None
    is_completed: Optional[int]=None
    due_date: Optional[Any]=None
    user_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: Optional[int]=None
    description: Optional[str]=None
    is_completed: Optional[int]=None
    due_date: Optional[Any]=None
    user_id: Optional[int]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    name: Optional[str]=None
    username: Optional[str]=None

    class Config:
        from_attributes = True

