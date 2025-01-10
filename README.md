## Blog application written using flask and templates!

for running locally, since I'm on windows I have to run using the following commands in sequence

    ### if the virtual environment hasn't been created
    python -m venv winvenv
    ### this creates a python virtual environment called winvenv (since im on windows)
    
    ### then, run the following to activate the python virtual environment in powershell
    .\winvenv\Scripts\activate

    ### ensure that flask is installed
    pip install flask

    ### set up the flask app so that it can be run (run the following in powershell)
    set FLASK_APP=blog.py

    ### run the app! (run the following to start up the app in powershell, and go to the url provided by the script on start-up)
    flask run

#### using python-dotenv

to configure environment variables, can pip install python-dotenv and set an environment variable for FLASK_APP using a .flaskenv file!

### note about databases!

When working with db servers like MySQL and Postgres, you'll have to create the db in the db server before running upgrade (if I plan to move to postgres!).

Also, if you want to name your own table names, add to the model class for a table the __tablename__ attribute to do so. Then you can name a table.

#### (Aside): db.session

check out the code below

    from app import app, db
    from app.models import User, Post
    import sqlalchemy as sa

    app.app_context().push()

    u = User(username='john', email='john@example.com')
    db.session.add(u)
    db.session.commit()

to commit changes to the database, do db.session.commit().
if there's an error, during a session, do db.session.rollback() to abort the session and remove any changes that were stored.

good idea to use the scalers method to get an iterator to get results of a query as opposed to the all method. scalers method gives an iterator wheras all gives a list which is less space efficient. Example below

    users = db.session.scalers(query)
    for u in users:
        print(u.id, u.username)

vs

    users = db.session.scalers(query).all()

##### flask shell

just run "flask shell" command to start a Python interpreter in the context of the application

    (winvenv) $ flask shell

#### (aside)

need to ensure windows system uses linefeed character when adding files to git. The following ensures when I'm checking out code (pulling) it converts linefeed characters to CRLF (carriage return, line feed) characters in case someone was working on linux while I'm working on windows

    $ git config --global core.autocrlf true

There's also the case where if I'm working on linux/mac you don't want git to auto convert on checkout. I can tell git to convert crlf to lf on commit, but not the other way around using the following command

    $ git config --global core.autocrlf input


when working on the application, set debug mode to true. This is helpful for getting more info when troubleshooting errors. To set it to true, do the following in the terminal:

for unix/linux/mac

    export FLASK_DEBUG=1

for windows (powershell)

    $env:FLASK_DEBUG="1"

to confirm that the debugger is working, when inputting the command "flask run" you should see that debug mode is set to "on". To turn the debugger off, just set it again to 0.

Setting the debugger on also enablesthe reloader, which automatically restarts the application anytime a source file is modified!

Be sure to disable debug mode when putting the app into production! The debugger allows the user to remotely execute code on the server!



