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
