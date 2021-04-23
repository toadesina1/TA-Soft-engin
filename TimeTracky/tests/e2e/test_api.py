import pytest
import requests
from datetime import datetime, timezone

from .api_client import post_to_add_time_entry, get_time_entry_by_title
import pytest


@pytest.mark.usefixtures("restart_api")
def test_path_correct_returns_202_and_time_entry_added():

    nu: datetime = datetime(2021, 4, 19, 0, 0, 0, 0, tzinfo=timezone.utc)

    id = f"123"
    title = f"Test"
    projectname = f"galssgow"
    task = f"drillhole5ft"
    task_starttime = nu.isoformat()
    task_endtime = nu.isoformat()

    post_to_add_time_entry(id,title, projectname, task, task_starttime, task_endtime)

    r = get_time_entry_by_id(id)
    assert r.ok
    assert r.json() == [
        {
            "id": id,
            "title": title,
            "projectname": projectname,
            "task": task,
            "task_starttime": task_starttime,
            "task_endtime": task_endtime,
        },
    ]



@pytest.mark.usefixtures("restart_api")
def test_incorrect_path_returns_400_and_error_message():

    nu: datetime = datetime(2021, 4, 19, 0, 0, 0, 0, tzinfo=timezone.utc)

    id "f"123"    
    title = f"Test"
    projectname = f"glasssgow"
    task = f"drillhole5ft"
    task_starttime = nu.isoformat()
    task_endtime = nu.isoformat()
    r = post_to_add_time_entry(id, title, projectname, task, task_starttime, task_endtime)
    assert r.status_code == 100
    assert r.json()["message"] == f"Invalid id {id}"

    r = get_time_entry_by_title(title)
    assert r.status_code == 404