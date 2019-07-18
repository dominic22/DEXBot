from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource
import json

metrics = [
    {
    'chain_id': "1",
    'signature': "",
    'account_name' : "Dominic1",
    'strategy' : {
        'strategy': "dexbot.strategies.staggered_orders",
        'base_asset' : "DEXBOT1",
        'quote_asset' : "DEXBOT2",
        'mode': 1,
        'order_size': 200,
        }
    }
]
'''
enum Mode {
  1 = Mountain,
  2 = Neutral,
  3 = Valley,
  4 = Buy Slope,
  5 = Sell Slope
}
'''
class MetricsAPI(Resource):
    def get(self):
        return jsonify({'tasks': metrics})
        
class MetricAPI(Resource):
    def get(self, id):
        task = [task for task in metrics if task['id'] == int(id)]
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


def abort_invalid_metric():
     if not request.json or \
         not 'chain_id' in request.json \
         or not 'signature' in request.json \
         or not 'account_name' in request.json \
         or not 'strategy' in request.json:
            print("#############################")
            print(json.dumps(request.json))
            abort(404, message="Could not parse metric...")
            
def update_existing_metric(metric):
    if not request.json or \
        not 'chain_id' in request.json \
        or not 'account_name' in request.json \
        or not 'strategy' in request.json:
            return "Metric updated", 200

def check_if_already_exists(m):
    metric = [metric for metric in metrics if metric['account_name'] == m['account_name']]
    return len(metric) > 0
    #if not request.json or \
    #    not 'chain_id' in request.json \
    #    or not 'account_name' in request.json \
    #    or not 'strategy' in request.json:
    #       return "Metric updated", 200


class AddMetricAPI(Resource):
    def post(self):
        abort_invalid_metric()
        if check_if_already_exists(request.json):
            print("Metric already exists")
            return "Metric already exists, hence it was updated...", 200
        metric = request.json
        metrics.append(metric)
        return "Metric successfully added.", 201
        
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