
import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)

from sqlalchemy.orm import registry, mapper, relationship

from timetrackylib.domain.models import time_entry

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = MetaData()

"""
Pure domain time_entry:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
ProjectName,TEXT NOT NULL,
Task TEXT NOT NULL,
StartTime TEXT,
EndTime TEXT NOT NULL,
Comment TEXT NULL,
"""
time_entry = Table(
    "time_entrys",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255)),
    Column("projectname", String(255)),
    Column("task", Text),
    Column("task_starttime", Text),
    Column("task_endtime", Text),
    Column("comment", Text),
)

def start_mappers():
    
    logger.info("starting mappers")
    # mapper_registry.map_imperatively(time_entry, time_entrys)
    mapper(time_entry, time_entrys)