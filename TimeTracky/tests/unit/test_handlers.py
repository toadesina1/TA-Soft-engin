from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from timetrackylib import bootstrap
from timetrackylib.domain import commands
from timetrackylib.services import handlers, unit_of_work
from timetrackylib.adapters import repository

from timetrackylib.adapters.orm import start_mappers
from timetrackylib.services.unit_of_work import FakeUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())


class TestAddtime_entry:
    def test_add_single_time_entry(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 4, 19, 13, 0, 5, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.Addtime_entryCommand(
                0,
                f"Test",  # title
                f"Glasgow",  # projectname
                nu.isoformat(),  # Task starttime
                nu.isoformat(),  # Task end time
        )

        assert bus.uow.time_entrys.get_by_title(f"Test") is not None
        assert bus.uow.committed

    def test_get_time_entry_by_id(self):
        bus = boostrap_test_app()

         nu: datetime = datetime(2021, 4, 19, 13, 0, 5, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.Addtime_entryCommand(
                99,
                f"Test",  # title
                f"Glasgow",  # projectname
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.time_entrys.get_by_id(99) is not None
        assert bus.uow.committed

    def test_get_time_entry_by_url(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 4, 19, 13, 0, 5, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.Addtime_entryCommand(
                99,
                f"Test",  # title
                f"Glasgow",  # projectname
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.time_entrys.get_by_projectname(f"Glasgow") is not None
        assert bus.uow.committed

    def test_get_all_time_entrys(self):
        bus = boostrap_test_app()

         nu: datetime = datetime(2021, 4, 19, 13, 0, 5, 0, tzinfo=timezone.utc)     
        bus.handle(
            commands.Addtime_entryCommand(
                99,
                f"Test",  # title
                f"Glasgow",  # projectname
                f"Drillhole5ft",  # task
                nu.isoformat(),  # task starttime
                nu.isoformat(),  # task endtime
            )
        )

        nuto = nu + timedelta(days = 3, hours=13)

        bus.handle(
            commands.Addtime_entryCommand(
                999,
                f"Test2",  # title
                f"Glasgow",  # projectname
                nu.isoformat(),  # task starttime
                nu.isoformat(),  # task endtime
            )
        )

        records = bus.uow.time_entry.get_all()
        assert len(records) == 2