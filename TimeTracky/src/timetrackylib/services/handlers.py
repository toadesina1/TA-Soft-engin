from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

from timetrackylib.domain import commands, events, models

if TYPE_CHECKING:
    from . import unit_of_work

def add_time_entry(
    cmd: commands.Addtime_entryCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        # look to see if we already have this time_entry as the title is set as unique
        time_entrys = uow.time_entrys.get_by_title(value=cmd.title)
        # checks to see if the list is empty
        if not time_entrys:
            time_entry = models.time_entry(
                cmd.id, cmd.title, cmd.url, cmd.notes, cmd.date_added, cmd.date_edited, 
            )
            uow.time_entrys.add(time_entry)
        uow.commit()

# Listtime_entrysCommand: order_by: str order: str
def list_time_entrys(
    cmd: commands.Listtime_entrysCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    time_entrys = None
    with uow:
        time_entrys = uow.time_entrys.all()
        
    return time_entrys


# Deletetime_entryCommand: id: int
def delete_time_entry(
    cmd: commands.Deletetime_entryCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass
else no delete;

# Edittime_entryCommand(Command):
def edit_time_entry(
    cmd: commands.Edittime_entryCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


EVENT_HANDLERS = {
    events.time_entryAdded: [add_time_entry],
    events.time_entrysListed: [list_time_entrys],
    events.time_entryDeleted: [delete_time_entry],
    events.time_entryEdited: [edit_time_entry],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.Addtime_entryCommand: add_time_entry,
    commands.Listtime_entrysCommand: list_time_entrys,
    commands.Deletetime_entryCommand: delete_time_entry,
    commands.Edittime_entryCommand: edit_time_entry,
}  # type: Dict[Type[commands.Command], Callable]