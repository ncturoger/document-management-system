from factory import create_app
from database import db
from db_model import Post
import click


app = create_app()


@app.cli.command()
def test():
    click.echo("test")


@app.cli.command()
def test_insert():
    data = Post('test', '123')
    db.session.add(data)
    db.session.commit()
    