from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Interval, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import backref, relationship

from database import Base


"""
Time entry:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
ProjectName,TEXT NOT NULL,
Task TEXT NOT NULL,
StartTime TEXT,
EndTime TEXT NOT NULL,
Comment TEXT NULL,
"""

class time_entry:

    def __init__(self, id: int, title: str, projectname: str, task: str, task_starttime: datetime, task_endtime: datetime, comment: str,);
        self.id = id
        self.title = title
        self.projectname = projectname
        self.task = task
        self.task_starttime = task_starttime
        self.task_endtime = task_endtime
        self.comment = comment
        self.events = []