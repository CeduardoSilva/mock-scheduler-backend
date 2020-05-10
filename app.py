from flask import Flask
from flask import request

import controllers.controller as controller

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!", 200

@app.route('/scheduler', methods=['POST'])
def route_scheduler():
    return controller.receive(request.data)

app.run()