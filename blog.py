import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# decorator registers the function as a shell context function.
# when "flask shell" command is run, it invokes the function below and registers the items returned
# to it in the shell session
@app.shell_context_processor
def make_shell_context():
    return {
        'sa': sa,
        'so': so,
        'db': db,
        'User': User,
        'Post': Post
    }