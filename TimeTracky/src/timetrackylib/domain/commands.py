"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from tpc import TPC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(TPC):
    pass


@dataclass
class Addtime_entryCommand(Command):
    """
    This command is a dataclass that encapsulates a time_entry
    This uses type hints: https://docs.python.org/3/library/typing.html
    """
    id: int
    title: str
    projectname: str
    task: str
    # data["starttime or endtime"] = datetime.utcnow().isoformat()
    task_starttime: str
    task_endtime: str
    comment: Optional[str] = None


@dataclass
class Listtime_entrysCommand(Command):
    order_by: str
    order: str


@dataclass
class Deletetime_entryCommand(Command):
    id: int


@dataclass
class Edittime_entryCommand(Command):
    id: int
    title: str
    projectname: str
    projectname: str
    task: str
    # data["starttime or endtime"] = datetime.utcnow().isoformat()
    task_starttime: str
    task_endtime: str
    comment: Optional[str] = None