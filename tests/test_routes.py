import os
import json
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
    # assert b'[]' in response.get_data()


def test_retrieve_task():
    url = root_url + "tasks/1"
    response = client.get(url)
    assert response.status_code == 200
    assert b'"id": 1' in response.get_data()

def test_create_task():
    url = root_url + "tasks"
    request_data = {
        "description": "hmmm",
        "id": "4",
        "title": "WOW AMZING"
    }
    response = client.post(url,
        data = json.dumps(request_data),
        content_type = 'application/json')
    assert response.status_code == 200
    assert "Success" or "Error" in response.get_data()

def test_update_task():
    url = root_url + "tasks/1"
    request_data = {
        "description": "hmmm"
    }
    response = client.put(url,
                data = json.dumps(request_data),
                content_type = 'application/json')

    assert response.status_code == 200

# def test_delete_task():
#     url = root_url + "tasks/1"
#     response = client.delete(url)
#     # assert response.status_code == 204