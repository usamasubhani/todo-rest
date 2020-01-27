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


    # Retrieve Tasks
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
        

    @app.route(base_url + "tasks/<task_id>", methods=['PUT'])
    def update_task(task_id):
        # req_task = json.loads(request.json)
        req_task = request.json
        task = Task.query.get(task_id)
        if not task_id:
            return "Task Not Found"
        if "title" in req_task.keys():
            task.title = req_task['title']
        if "description" in req_task.keys():
            task.description = req_task['description']
        if "status" in req_task.keys():
            if req_task['status'] == "True":
                task.status = True
            elif req_task['status'] == "False":
                task.status = False
            # task.status = bool(req_task['status'])
        db.session.commit()
        # for key in req_task.keys():
        #     task.
        return "Success", 201
        

    # Delete Task
    # @app.route(base_url + "tasks/<task_id>", methods=['DELETE'])