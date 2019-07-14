from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


class MetricsAPI(Resource):
    def get(self):
        return jsonify({'tasks': tasks})
        
class MetricAPI(Resource):
    def get(self, id):
        task = [task for task in tasks if task['id'] == int(id)]
        if len(task) == 0:
            print("ABORT")
            abort(404)
        return jsonify({'task': task[0]})
    '''def put(self):
        if not request.json or not 'title' in request.json:
            abort(400)
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201
'''

'''
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
'''

class AddMetricAPI(Resource):
    def post(self):
        if not request.json or not 'title' in request.json:
            abort(404)
        task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'description': request.json.get('description', ""),
            'done': False
        }
        tasks.append(task)
        return jsonify({'task': task}), 201

        
'''
@app.route('/v1.0/metrics', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/v1.0/metrics/<int:metric_id>', methods=['GET'])
def get_task(metric_id):
    task = [task for task in tasks if task['id'] == metric_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/v1.0/metrics', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

'''