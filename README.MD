# Flask Tutorial

This is a walkthrough using the [Flask Tutorial for version 1.1.x](https://flask.palletsprojects.com/en/1.1.x/tutorial/).

**NOTE:** the final branch `test_coverage` contains the fully-completed tutorial.

[miniconda](https://docs.conda.io/en/latest/miniconda.html) was used for virtual environment management.

The following conda command is used to create the virtual environment:

`conda create -n flask_tutorial python=3.9`

## Git Basics

As I will create branches for each phase of the tutorial, I first review some git basics.

### Initialization

We need to initialize the repository so that git can track changes in a given folder (and its subfolders)

`git init`

### Cloning

In many cases, such as with the [Flask tutorial](https://github.com/pallets/flask/tree/1.1.2/examples/tutorial), it may be just as easy to clone an existing repository.

You can clone a repo with this command:

`git clone /path/or/url/to/repository`

or

`git clone user@host:/path/to/repository`

### Add and Commit

You add files to be tracked by git, which means you do not have to mark all files for tracking.

You can also use a `.gitignore` file to specify explict files or patterns of files to be excluded from tracking.

#### Adding

If you want to add a specific file:

`git add <filename>`

IF you want to add some pattern:

`git add *.xml`

Or, just add it all

`git add -A`

#### Commits

Now that git is tracking changes in your files, you can periodically "save" these changes by commmiting them.

This is not the same thing as saving the file, it is saving the current state of the file(s) for the purposes of change tracking.  As sucn, git only tracks changes.

`git commit -m 'commit message`

#### Working with Remote Peers

Git doesn't use a central server architecture for version control, but many web-based services, such as Github, exist to provide a means of coordinating your local changes with a remote server.  This is one of the means by which more than one developer can share that codebase and work together through a shared remore repository.

The way that we establish a remote is with this command:

`git remote add origin <server_url>`

In this example, **origin** is the label/name you create to refer to the URL for the remote repository.

Now, when you want the remote repository to match the changes you've made locally, you issue this command:

`git push origin master`

Conversely, when you want the current state of the remote to be reflected in your local version, you issue this command:

`git pull origin master`

In this case, you are seeking to merge those changes into your local version and to be notified if there are conflicts.

#### Branching

Another strategy is to use branching to isolate a set of changes from the rest fo the repository.  This is useful for versioning and also for collaborators to avoid stepping on each other.

You can create a branch this way:

`git checkout -b name_of_branch`

You can see that **checkout** is the way to select a branch to "move" to and the **-b** option is the way to provide the name of the branch. If the branch doesn't exist it will be created.  Now, all changes you make to the codebase will be in that branch and not in the msater.

If you not longer need a branch, it can be deleted:

`git branch -d name_of_branch`

#### Merging

Eventually, it is common that you'll want to rejoin a branch to the main branch or otherwise merge one version into another.  Thie command to do so is:

`git merge <branch>`

The way this works is as follows:

You always are in a current branch and you can change in one of serveral ways:

`git status`

This will tell you quite a bit about the current state of your respository, but it will also tell you what branch is active.

It is also common for your git installation to modify the command interpreter/environment to show the name of the current branch as a part of the prompt.

So, the when you specify `git merge <branch>` you are saying "take the branch I name here and merge it INTO the current active branch."

## Flask Tutorial

Any salient notes about a section of the tutorial appears here.

### Project Layout

This portion of the tutorial explains the anatomy of a typical Flask application by example.

![project layout](/images/project_layout.PNG)

The need for a [good .gitignore file](https://github.com/github/gitignore/blob/master/Python.gitignore) is also emphasized.

### Application Setup

The simplicity of Flask is that a singleton Flask object handles the functions of the pogram and framework.

It is necessary to install flask using pip: `pip install flask`

However, the tutorial takes a more sophisticated approach using a __init__.py file to initialze the Flask object for the entire package.

The tutorial has us place all application code (app is called **flaskr**) into a dedicated subdirectory: `flaskr`

Then the Flask object/app is initialized thusly:

```python
import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
```

Tres elegant!

#### Environment Variables

Also, I am using **python-dotenv** to manage environment variables for the app.

`pip install python-dotenv`

Once installed, we use this code to read the .env file:

```python
from dotenv import load_dotenv
load_dotenv()
```

The tutorial directs that we utilize the following environment variables:

* FLASK_APP=flaskr
* FLASK_ENV=development


### SQLite_database

The tutorial uses Python's built-in sqlite3 module to work directly with SQLite and SQL.

This is handled in a module within flaskr called `db.py`:

```python
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

Since the tutorial shows a manual and "hand crafted" approach to working directly with SQLite, we also utilize some basic SQL DDL:

```SQL
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

the database module is extended with these functions:

```python
# in the db.py module
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```

Tigher integration with Flask is possible with these additions:

```python
# in the __init__.py module
def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

Now, the `flask init-db` command can be run

### Blueprints and Views

Flask does a degree of namespacing with the concept of a blueprint which aggregates views and code to be used together.  The documentation indicates that these are blueprints as they shape how an app can be made within the broader flask app.

In this case, an `auth` blueprint will be created to handle the related facilities of providing authentication and authorization.

An `auth.py` module is created:

```python
# in the auth.py module
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')
```

As was the case with the database, this blueprint is registered with the Flask app in the `create_app` factory method:

```python
    # included in the create_app factory method
    from . import auth
    app.register_blueprint(auth.bp)
```

#### View?

A view is part of the MVC pattern that simply suggests how Flask pairs a route dectorator with the code that should be run when the route is matched.

This may be evident in the following register view defined in the `auth.py` module:

```python
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
```

Other views are specified as required to complete the blueprint.

We can also set a decorator function to be used to establish authorization for an authenticated user:

```python
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
```

### Templates

While those useing Flask to create a REST API may not use Jinja2 templates to generate HTML, the concepts are still useful.

A template is a means of generating output such that logic-driven dynmic data can be interspersed within static content, such as HTML.

Flask uses the [Jinja2 templating engine for Python](https://jinja.palletsprojects.com/en/2.11.x/).  Most templating engines are very similar to one another.

```html
<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1>Flaskr</h1>
  <ul>
    {% if g.user %}
      <li><span>{{ g.user['username'] }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>
```

You can see that the template tags `{% %}` are used to escape the static content to provide dynamic content in place of the tag.

Here is the template for user registration:

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="post">
    <label for="username">Username</label>
    <input name="username" id="username" required>
    <label for="password">Password</label>
    <input type="password" name="password" id="password" required>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

In particular, jinja2 and the [Django Template Language](https://docs.djangoproject.com/en/3.1/ref/templates/language/) are very similar.

### Static Files

Flask has a straight-forward means of supporting static files.  The convention is: `{{ url_for('static', filenam='name_of_file')}}`

### Blog Blueprint

Most of the fundamentals of Flask can be applied in this simple Blog Blueprint.  In particular, our ability to create, read, update, and delete records of a type is a key semantic in most web appliications.

The blueprint uses a familiar pattern:

```python
# in the blog.py module
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)
```
#### READ

The index view of most apps will be the READ component of CRUD.

```python
# in the blog.py module
@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
```

The sqlite package in Python provides a convenient way of working with data

The index template demonstrates how Jinga2 facilitates some basic programming structures within the template:

```html
{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{ url_for('blog.create') }}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}</div>
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
      <hr>
    {% endif %}
  {% endfor %}
{% endblock %}
```

#### CREATE

We will always use HTML forms for input and the means by which we work with a form can be see in the view and template for the `/create` route:

```python
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')
```

## Make installable

The step in the tutorial about making the project installable is vital to follow or testing won't work.

Key components are:
* setup.py
* `pip install -e .`

```python
# in setup.py
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
```

### Test Coverage

The Flask tutorial mentions testing, although admittedly and curiously at the end of the tutorial.

As we have already done in previous work, the Flask tutorial uses the `pytest` package as well as `coverage` in order to track how thoroughly the application is tested.

The testing the Flask tutorial does not use the level of architecture for extensibility that would be ideal, but it does show testability.

First, we install the packages:

```bash
pip install pytest coverage
```

As we have discussed previously, the tests for flaskr use `pytest` and utilize a `conftest.py` module to declate setup and fixtures for the tests.

Ideally, and this is demonstrated in the tutorial, you would organize your tests to reflect the structure of the project.  Therefore, the tutorial develops a one to one mapping between application modules and test modules:

* factory
* database
* authentication
* blog

Pytest can be supplied a `setup.cfg` file to make running tests for the project more compact and direct.

```
[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source = flaskr
```

The commands to run now are simple:
* `pytest` this will use the `setup.cfg` file to run all of the tests in each test module
* `coverage` this will give a report on testing coverage for the projuect.

You can run `coverage html` to get the coverage reports as a web page.