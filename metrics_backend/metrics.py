from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource
import json

metrics = []

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
        return jsonify({'metrics': metrics})

def getSummedMetrics():
    '''
        staggered_order : {
            strategy: string
            amount: number
        }
    '''
    summedMetrics = {}
    if len(metrics) == 0:
        return metrics
    for metric in metrics:
        strategy = metric["strategy"]["module"]
        print("_____________________________ FOR EACH" + strategy)
        if strategy in summedMetrics:
            print ("1111111111111111Add newwwwwwwwwwwwwww " + strategy)
            amount = summedMetrics[strategy]["amount"]
            summedMetrics[strategy]["amount"] = metric["amount"] + amount
        else:
            print ("1111111111111111Add metric to map " + strategy)
            summedMetrics[strategy] = {
                "strategy": strategy,
                "amount": metric["amount"],
            }
    print("###################SUMMED ", jsonify(summedMetrics))
    return summedMetrics        

class StatisticsAPI(Resource):
    def get(self):
        return jsonify({'metrics11': getSummedMetrics()})
        
class MetricAPI(Resource):
    def get(self, id):
        task = [task for task in metrics if task['id'] == id]
        if len(task) == 0:
            print('Account was not found...')
            return "Account was not found...", 204
        return jsonify({'task': task[0]})

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
            return 'Metric updated.', 200

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


class RemoveMetricAPI(Resource):
    def post(self):
        abort_invalid_metric()
        if check_if_already_exists(request.json):
            print("Metric found, thus will be removed...")
            print("TODO remove metric")
            return "Metric successfully removed...", 200
        else:
            return "Metric does not exist.", 204
