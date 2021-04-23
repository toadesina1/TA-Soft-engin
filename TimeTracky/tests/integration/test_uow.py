import threading
import time
import traceback
from datetime import datetime, timezone
from typing import List
from unittest.mock import Mock
import pytest
from timetrackylib.domain.models import time_entry
from timetrackylib.services import unit_of_work

pytestmark = pytest.mark.usefixtures("mappers")

# self.id = id
# self.title = title
# self.projectname = projectname
# self.task = task
# self.task_starttime = task_starttime
# self.task_endtime = task_endtime
        
def insert_time_entry(id: int, title: str, projectname: str, task: str, task_starttime: str, task_endtime: str,comment: str=None, ):
    session.execute(
        """
        INSERT INTO time_entry (id, title, projectname, task, task_starttime, task_endtime,comment) 
        VALUES (:id, :title, :projectname, :task, :task_starttime, :task_endtime,comment)
        """,
        dict(
	    id=id,            
            title=title, 
            projectname=projectname,
            task=task,
            task_starttime=task_starttime,
            task_endtime=task_endtime,
            comment=comment,
        ),
    )

def test_can_retreive_time_entry(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 4, 19, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_time_entry(123, f"Test", Glasgow", nu.isoformat(), nu.isoformat())
    session.commit()

    time_entry: time_entry = None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        time_entry = uow.time_entrys.get_by_title(f"Test")
        assert time_entry.title == f"Test"
        # uow.commit()

    # assert time_entry.title == f"Test"