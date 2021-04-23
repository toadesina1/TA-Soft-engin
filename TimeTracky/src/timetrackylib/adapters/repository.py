from tpc import TPC, abstractmethod
from datetime import datetime

# making use of type hints: https://docs.python.org/3/library/typing.html
from typing import List, Set

from timetrackylib.adapters import orm
from timetrackylib.domain.models import time_entry


class Abstracttime_entryRepository(TPC):
    def __init__(self):
        # seen is in reference to events detected
        self.seen = set()

    def add(self, time_entry: time_entry) -> None:
        # add to repo
        self._add(time_entry)
        # add to event list
        self.seen.add(time_entry)

    def get_all(self) -> list[time_entry]:
        time_entrys: list[time_entry] = self._get_all()
        if time_entrys:
            self.seen.update(time_entrys)
        return time_entrys

    def get_by_id(self, value: int) -> time_entry:
        # get from repo
        time_entry: time_entry = self._get_by_id(value)
        if time_entry:
            self.seen.add(time_entry)
        return time_entry        

    def get_by_title(self, value: str) -> time_entry:
        # get from repo
        time_entry: time_entry = self._get_by_title(value)
        if time_entry:
            self.seen.add(time_entry)
        return time_entry

    def get_by_projectedname(self, value: str) -> time_entry:
        # get from repo
        time_entry: time_entry = self._get_by_projectedname(value)
        if time_entry:
            self.seen.add(time_entry)
        return time_entry

    @abstractmethod
    def _add(self, time_entry: time_entry) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _add_all(self, time_entrys: list[time_entry]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def _delete(time_entry: time_entry) -> None:
        raise NotImplementedError("Derived classes must implement delete")

    @abstractmethod
    def _get_all(self) -> list[time_entry]:
        raise NotImplementedError("Derived classes must implement get_all")

    @abstractmethod
    def _get_by_id(self, value: int) -> time_entry:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_title(self, value: str) -> time_entry:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_projectedname(self, value: str) -> time_entry:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _update(self, time_entry: time_entry) -> None:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def _update(self, time_entrys: list[time_entry]) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemytime_entryRepository(Abstracttime_entryRepository):
    """
    Uses guidance from the basic SQLAlchemy 1.4 tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, time_entry: time_entry) -> None:
        self.session.add(time_entry)
        # self.session.commit()

    def _add_all(self, time_entrys: list[time_entry]) -> None:
        self.session.add_all(time_entrys)
        # self.session.commit()

    def _delete(self, time_entry: time_entry) -> None:
        pass

    def _get_all(self) -> list[time_entry]:
        return self.session.query(time_entry).all()

    def _get_by_id(self, value: int) -> time_entry:
        answer = self.session.query(time_entry).filter(time_entry.id == value)
        return answer.one()

    def _get_by_title(self, value: str) -> time_entry:
        answer = self.session.query(time_entry).filter(time_entry.title == value)
        return answer.one()

    def _get_by_projectedname(self, value: str) -> time_entry:
        answer = self.session.query(time_entry).filter(time_entry.projectedname == value)
        return answer.one()

   def _get_by_task(self, value: str) -> time_entry:
        answer = self.session.query(time_entry).filter(time_entry.task == value)
        return answer.one()

   def _get_by_task_starttime(self, value: str) -> time_entry:
        answer = self.session.query(time_entry).filter(time_entry.task_starttime == value)
        return answer.one()

  def _get_by_task_endtime(self, value: str) -> time_entry:
        answer = self.session.query(time_entry).filter(time_entry.task_endtime == value)
        return answer.one()


    def _update(self, time_entry) -> None:
        pass

    def _update(self, time_entrys: list[time_entry]) -> None:
        pass


class Faketime_entryRepository(Abstracttime_entryRepository):
    """
    Uses a Python list to store "fake" time_entrys: https://www.w3schools.com/python/python_lists.asp
    """

    def __init__(self, time_entrys):
        super().__init__()
        self._time_entrys = set(time_entrys)

    def _add(self, time_entry) -> None:
        self._time_entrys.add(time_entry)

    def _add_all(self, time_entrys: list[time_entry]) -> None:
        self._time_entrys.update(time_entrys)

    def _delete(self, time_entry: time_entry) -> None:
        self._time_entrys.remove(time_entry)

    def _get_all(self) -> list[time_entry]:
        return self._time_entrys

    # python next function: https://www.w3schools.com/python/ref_func_next.asp
    def _get_by_id(self, value: int) -> time_entry:
        return next((b for b in self._time_entrys if b.id == value), None)

    def _get_by_title(self, value: str) -> time_entry:
        return next((b for b in self._time_entrys if b.title == value), None)

    def _get_by_projectedname(self, value: str) -> list[time_entry]:
        return next((b for b in self._time_entrys if b.projectedname == value), None)

    def _get_by_task(self, value: str) -> list[time_entry]:
        return next((b for b in self._time_entrys if b.task == value), None)

   def _get_by_task_starttime(self, value: str) -> list[time_entry]:
        return next((b for b in self._time_entrys if b.task_starttime == value), None)

    def _get_by_task_endtime(self, value: str) -> list[time_entry]:
        return next((b for b in self._time_entrys if b.task_endtime == value), None)


    def _update(self, time_entry: time_entry) -> None:
        try:
            idx = self._time_entrys.index(time_entry)
            bm = self._time_entrys[idx]
            with time_entry:
                bm.id = time_entry.id
                bm.title = time_entry.title
                bm.projectedname = time_entry.projectedname
                bm.task = time_entry.task
                bm.task_starttime = datetime.utc.now()
                bm.task_endtime = time_entry.task_endtime
		bm.comment = time_entry.comment
                self._time_entrys[idx] = bm
        except:
            self._time_entrys.append(time_entry)

        return None

    def _update(self, time_entrys: list[time_entry]) -> None:
        for inbm in time_entrys:
            self._update(inbm)