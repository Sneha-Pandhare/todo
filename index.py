from flask import Flask, render_template, request
import ssl
from pymongo import MongoClient
client = MongoClient("mongodb+srv://snehap:vRoMDciclQXZY04E@cluster0.yuso4.mongodb.net/todo?retryWrites=true&w=majority",ssl=True,ssl_cert_reqs=ssl.CERT_NONE)
todo_db = client['todo']
todos_collection = todo_db['todos']
flask_app = Flask(__name__)
todos = []
@flask_app.route('/',methods=['POST', 'GET'])
def sendHomePage():
    if (request.method == 'POST'):
        todo = request.form.get('todo')
        todo_d = {}
        todos.append(todo)
        todo_d['name'] = todo
        todos_collection.insert_one(todo_d)
    return render_template('home.html', todos = todos_collection.find())

flask_app.run('0.0.0.0', 5000)