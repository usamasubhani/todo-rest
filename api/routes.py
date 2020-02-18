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

    @app.route("/todo/api/v1.0/tasks")
    def tasks_list():
        t = Task.query.all()
        tasks = []
        for task in t:
            t_dict = task.__dict__ ## TO-DO : Use vars
            t_dict.pop('_sa_instance_state')
            tasks.append(t_dict)
        return json.dumps(tasks)

    @app.route(base_url + "tasks/<task_id>")
    def get_task(task_id):
        task = Task.query.filter_by(id=task_id).first()
        if not task:
            return json.dumps("{}")
        vars(task).pop('_sa_instance_state')
        return json.dumps(vars(task))

    @app.route(base_url + "tasks", methods=['POST'])
    # def new_task():
    #     task = request.json
    #     found = Task.query.filter_by(id=task['id']).first()
    #     if not found:
    #         t = Task(id = task['id'],
    #                 title = task['title'],
    #                 description = task['description'],
    #                 status = False)
    #         db.session.add(t)
    #         db.session.commit()
    #         return "Task Added Successfully"
    #     else:
    #         return "Error: Task with same ID Already exists!!"
    def new_task():
        task = request.json
        # found = Task.query.filter_by(id=task['id']).first()
        # if not found:
        print(task)
        t = Task(title = task['title'],
                description = task['description'],
                status = False)
        db.session.add(t)
        db.session.commit()
        return tasks_list()
        # return "SUCCESSS", 200
        
        

    @app.route(base_url + "tasks/<task_id>", methods=['PUT'])
    def update_task(task_id):
        req_task = request.json
        task = Task.query.get(task_id)
        
        if not task:
            return "Task Not Found"

        if "title" in req_task.keys():
            task.title = req_task['title']
        if "description" in req_task.keys():
            task.description = req_task['description']
        if "status" in req_task.keys():         
            if req_task['status']:
                task.status = True
            elif req_task['status']:
                task.status = False

        db.session.commit()

        return tasks_list(), 200
        

    # Delete Task
    @app.route(base_url + "tasks/<task_id>", methods=['DELETE'])
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if not task:
            return "Task Not Found", 200
        db.session.delete(task)
        db.session.commit()
        return tasks_list(), 202
