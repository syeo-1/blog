from app import app

@app.route('/')
@app.route('/index')
def inex():
    return 'hello, world!'