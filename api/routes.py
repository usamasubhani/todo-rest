# from api import app
import json
from flask import request
# from api import db
from api.model import Task

def config_routes(app, db):
    
    base_url = "/todo/api/v1.0/"
    
    @app.route('/')
    def root():  
        return "Hello Worldddd"


    @app.route(base_url + "tasks")
    def tasks_list():
        t = Task.query.all()
        tasks_dict = {"tasks":[]}
        for task in t:
            t_dict = task.__dict__ ## TO-DO : Use vars
            t_dict.pop('_sa_instance_state')
            tasks_dict["tasks"].append(t_dict)
        return json.dumps(tasks_dict)


    @app.route(base_url + "tasks/<task_id>")
    def get_task(task_id):
        task = Task.query.filter_by(id=task_id).first()
        if not task:
            return json.dumps("{}")
        vars(task).pop('_sa_instance_state')
        return json.dumps(vars(task))

    @app.route(base_url + "tasks", methods=['POST'])
    def new_task():
        task = request.json
        found = Task.query.filter_by(id=task['id']).first()
        if not found:
            t = Task(id = task['id'],
                    title = task['title'],
                    description = task['description'],
                    status = False)
            db.session.add(t)
            db.session.commit()
            return "Task Added Successfully"
        else:
            return "Error: Task with same ID Already exists!!"