from datetime import date, datetime, timedelta
import random

from timetrackylib.domain import events
from timetrackylib.domain.models import time_entry

ok_urls = ["http://", "https://"]


def test_time_entry_title_is_unique():
    pass

def test_authentication_of_users():

    # arrange
    created: str = email, nullable=False ()
            str = password, nullable=False ()

    # act
    autehmticate: str = created
    login = login(amen@wtam.edu, "bubususu")

    # assert
    assert authetication.login == time_entry.login

def test_new_time_entry_task_starttime_and_task_endtime_are_the_same():
    # arrange
    created: str = datetime.now().isoformat()

    # act
    edited: str = created
    time_entry = time_entry(123, "test", "Glasgow", "None", "created", "created")

    # assert
    assert time_entry.task_startime == time_entry.task_endtime


def test_new_time_entry_task_is_well_formed():
    # arrange
    created: str = datetime.now().isoformat()
    edited: str = created

    # act
    time_entry = time_entry(123, "test", "Glasgow", None, created, edited)
    # list comprehensions - https://www.w3schools.com/python/python_lists_comprehension.asp
    okay = [prefix for prefix in ok_projectname if time_entry.projectname.startswith(prefix)]
    # any function - https://www.w3schools.com/python/ref_func_any.asp
    assert any(okay)


def test_that_edit_time_is_newer_than_created_time():
    # arrange
    created: str = datetime.now().isoformat()
    edited: str = created

    # act
    time_entry = time_entry(123, "test", "Glasgow", None, created, edited)

    time_entry.comment = "Lorem Ipsum"
    hours_addition = random.randrange(1, 10)
    tast_starttime = datetime.fromisoformat(time_entry.tast_starttime)
    time_entry.tast_starttime= (task_starttime + timedelta(hours=hours_addition)).isoformat()

    # assert
    assert time_entry.task_endtime < time_entry.task_endtime