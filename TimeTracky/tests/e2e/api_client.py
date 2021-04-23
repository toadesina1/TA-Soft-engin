import requests
from timetrackylib import config


def post_to_add_time_entry(
    id: int,
    title: str,
    projectedname: str,
    task: str,
    task_starttime: str,
    task_endtime: str,
    comment: str,
):
    url = config.get_api_url()

    # self.id= id
    # self.title = title
    # self.prjectname = projectname
    # self.task = task
    # self.task_startime = task_starttime
    # self.task_endtime = task_endtime
    # self.comment = comment


    r = requests.post(
        f"{url}/add_time_entry",
        json={
            "id": id,
            "title": title,
            "projectedname": projectedname,
            "task_starttime": task_starttime,
            "task_endtime": task_endtime,
            "comment": comment,
        },
    )
    assert r.status_code == 201


def get_time_entry_by_id(id: str):
    taks = config.get_api_task()
    return requests.get(f"{task}/time_entrys/{title}")