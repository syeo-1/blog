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


