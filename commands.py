import click
from flask.cli import with_appcontext

from api import db
from api.model import Task

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()