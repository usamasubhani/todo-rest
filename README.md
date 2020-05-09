# todo-webservice

### Running

```bash
git clone https://github.com/usamasubhani/todo-webservice.git
cd todo-webservice
pip install --user --requirement requirements.txt
export FLASK_APP=api
export FLASK_ENV=development
flask run
```

### Using Docker
```bash
git clone https://github.com/usamasubhani/todo-webservice.git
cd todo-webservice
docker build -t todo-microservice:latest .
docker run -it -p 5000:5000 todo-microservice
```



### Methods

| Method | URI                                                 | Action                |
| ------ | --------------------------------------------------- | --------------------- |
| GET    | /todo/api/v1.0/tasks           | Get list of all tasks |
| GET    | /todo/api/v1.0/tasks/<task_id> | Get a task            |
| POST   | /todo/api/v1.0/tasks/          | Create task           |
| PUT    | /todo/api/v1.0/tasks/<task_id> | Update task           |
| DELETE | /todo/api/v1.0/tasks/<task_id> | Delete task           |



### Libraries

- Flask
- Flask-SQLAlchemy
- flask-cors
- pytest


### Database
Single table PostgresSQL database with following columns:
- id
- title
- description
- status
