from timetrackylib.services import unit_of_work


def time_entry_view(id: int, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT id, projectname, task FROM time_entry WHERE id = :id
            """,
            dict(id=id),
        )
    return [dict(r) for r in results]