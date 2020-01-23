from todo-webservice import app

@app.route(/)
def get():
    print("Hello World")