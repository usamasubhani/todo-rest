import os
from flask import Flask
import pytest
from api.routes import config_routes
from api.config import Config
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# @pytest.fixture
# def client():
    
root_url = "/todo/api/v1.0/"

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
config_routes(app, db)
client = app.test_client()

def test_base_route():    
    url = "/"
    response = client.get(url)
    assert b'Hello' in response.get_data()
    assert response.status_code == 200

def test_tasks_list():
    url = root_url + "tasks"
    response = client.get(url)
    assert response.status_code == 200
    assert b'tasks' in response.get_data()


def test_retrieve_task():
    pass

def test_create_task():
    pass

def test_update_task():
    pass

def test_delete_task():
    pass
