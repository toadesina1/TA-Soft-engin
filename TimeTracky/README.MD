TimeTracky is inspired by the components of the APP Book's architecture that demonstrates some basic software engineering principles such as:

* Separation of concerns
* Loose Coupling
* Inheritance
* Extensibility
* Abstraction
* Refactoring

The repository is an extension of Dane's example that also include testing.

Layered Architecture
    At a basic level, the architecture is designed with a layered strategy to include the following common/typical elements:

* Presentation Layer (will be a module called models.py here)
* Business Logic Layer (will be a module called commands.py here)
* Presistence Layer (will be a module called repository.py here)

# Bare Bones Approach

## Persistence
We will take a bare bones approach and connect it directly to a sqlite database.

The DB Browser for SQLite tool will be useful to inspect the data and manage the database file. SQLiteStudio is another alternative that would accomplish the same thing.

The initial database wil consist of a table called time_entry:

``` sql
CREATE TABLE IF NOT EXISTS time_entry
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    ProjectName,TEXT NOT NULL,
    Task TEXT NOT NULL,
    Task_StartTime TEXT,
    Task_EndTime TEXT NOT NULL,
    Comment TEXT NULL,
);
```


The TimeTracky factored using;

SQLAlchemy O/RM that will handle our data
Completed the implicit and explicit promises of the existing API
We use web-based REST API
Use looser coupling
Improve architecture by using:
SOLID
Repository Pattern and Unit of Work (understand how SQLAlchemy is really doing this)
Dependency injection
SQLAlchemy 1.4.x

After following the APP architecture, we will validate and justify the code through functional testing that includes;
* Unit Tests
* Integration Tests
* End-to-End Tests

### Report Section

There are four sections in the report, each one is a aggregated view of the previous one.

1. Summary: shows the report date and the total working and break time.

2. Projects: groups activities by project. This is useful to track the
total time by projects. We specify the project for an activity.

3. Tasks: groups tasks by name. This is useful to track the
total time worked on a task when you have worked on it multiple times.

4. Details: timeline of your activities.


For example, you entered the activities below throughout the day:

$ add "project-1: task-3"
$ add "project-2: task-2"
$ add "project-1: task-1"
$ add "lunch **"
$ add "project-2: task-2"
$ add "project-1: task-2"
```

And then you view your timesheet:

```
$ report

----------------------- Monday, April 19, 2021 (week 18) -----------------------

Working Time: 7h00
Break   Time: 1h00

----------------------------------- Projects -----------------------------------

(5h00) project-1: task-1, task-2, task-3
(2h00) project-2: task-2

---------------------------------- Activities ----------------------------------

(2h15) project-1: task-1
(2h15) project-1: task-2
(0h30) project-1: task-3
(2h00) project-2: task-2

(1h00) : lunch **

----------------------------------- Details ------------------------------------

(0h30) 09:00-09:30 project-1: task-3
(0h15) 09:30-09:45 project-2: task-2
(2h15) 09:45-12:00 project-1: task-1
(1h00) 12:00-13:00 lunch **
(1h45) 13:00-14:45 project-2: task-2
(2h15) 14:45-17:00 project-1: task-2

The first section, the summary section, shows that you worked 7h and
had a 1-hour break.

Then, the projects section shows that you worked 5h on project 1 and
2h on project 2. You can specify the project of an activity by
prefixing it with a non-whitespace string followed by a colon (e.g
`project-1:`, `project2:`).

The next section, the activities section, shows how long you worked on
each activity. For instance, even though you worked twice on
`project-2: task-2` (0h15 + 1h45), it is shown once in that section.

Finally, the details section shows a timeline of all your activity.


#pytest

The validation and justification should ensure that;

Users can access the site and create an account, made unique by their email address and secured by a password.

On the portfollio, users can see which project they are currently working on, task assigned and when they started on it. They can also switch to 
a different project (and are given choices of existing projects, or an option to create a new one) or cease working.

On the history page, users are presented with a list of the projects they have worked on for the current day, and how many hours they have spent. 
The project manager have module to review the time entry of other users and rate the them accordginly. They also have right to assign task to site workers.
