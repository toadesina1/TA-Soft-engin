from datetime import datetime
from sqlalchemy import create_engine
from flask import Flask, jsonify, request
from timetrackylib.adapters.orm import start_mappers, metadata
from timetrackylib.domain import commands
from timetrackylib.api import views
from timetrackylib import bootstrap

app = Flask(__name__)
bus = bootstrap.bootstrap()

@app.route('/')
def index(self):
    return f'timetracky API'

# add admin 
@app.route('/add_time_entry', methods=['POST'])
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

    return f'timetracky API

#add authentication 
@app.route('/add_time_entry', methods=['POST'])
@login_required
    __tablename__ = "time_entry"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    projects = relationship("Project", order_by="Project.name", backref="user")

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "<User {0} (hashed password: {1})>".\
                format(self.email, self.password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def check_password(self, entered_password):
        return check_password_hash(self.password, entered_password)

@app.route('/add_time_entry', methods=['POST'])
def add_time_entry():
    # id, title, projectname, task, task_starttime , task_endtime
    id = request.json["id"] 
    title = request.json["title"]
    projectname = request.json["projectname"]
    task = request.json["task"]
    task_starttime = request.json["task_starttime"]
    task_endtime = request.json["task_entime"]
    comment = request.json["comment"]

    cmd = commands.Addtime_entryCommand(
            id, title, projectname, task, task_starttime , task_endtime, comment 
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/time_entrys/<id>", methods=['GET'])
def get_time_entry_by_title(self, id):
    result = views.time_entrys_view(id, bus.uow)
    if not result:
         return "not found", 404
    return jsonify(result), 200

def get_time_entry_by_id(self, id):
    pass

def delete(self, time_entry):
    pass

def update(self, time_entry):
    pass

if __name__ == "__main__":
    app.run()