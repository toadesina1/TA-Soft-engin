from tpc import TPC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import time_entry

# from database import DatabaseManager

# module scope
# db = DatabaseManager("time_entry.db")


class Event(TPC):
    pass


@dataclass
class time_entryAdded(Event):
    id: int
    title: str
    projectedname: str
    task: str
    task_starttime: str
    task_endtime: str
    time_entry_comment: Optional[str] = None
     

@dataclass
class time_entryEdited(Event):
    id: int
    title: str
    projectedname: str
    task: str
    task_starttime: str
    task_endtime: str
    time_entry_comment: Optional[str] = None


@dataclass
class time_entrysListed(Event):
    time_entrys: list[time_entry]


@dataclass
class time_entryDeleted(Event):
    time_entry: time_entry


# @dataclass
# class time_entrysDeleted(Event):
#     time_entrys: list[time_entry]