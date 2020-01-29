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



### Methods

| Method | URI                                           | Action                |
| ------ | --------------------------------------------- | --------------------- |
| GET    | http://localhost:5000/todo/api/v1.0/          | Get list of all tasks |
| GET    | http://localhost:5000/todo/api/v1.0/<task_id> | Get a task            |
| POST   | http://localhost:5000/todo/api/v1.0/          | Create task           |
| PUT    | http://localhost:5000/todo/api/v1.0/<task_id> | Update task           |
| DELETE | http://localhost:5000/todo/api/v1.0/<task_id> | Delete task           |



### Libraries

- Flask
- Flask-SQLAlchemy
- pytest


### Database
Single table SQLite database with following columns:
- id
- title
- description
- status
