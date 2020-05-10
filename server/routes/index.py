from server import app
from flask import render_template
from flask import request

import random
import controllers.controller as controller

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')

@app.route('/scheduler', methods=['POST'])
def route_scheduler():
    return controller.receive(request.data)

@app.route('/testando', methods=['POST'])
def route_testando():
    print("BATEU AE")
    return controller.receive(request.data)

#http://afbc2de9.ngrok.io
#https://mock-scheduler-backend.mybluemix.net/scheduler/