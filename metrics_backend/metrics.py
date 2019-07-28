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

def getInverseMarket(market):
    splittedMarket = market.split('/')
    return splittedMarket[1] + "/" + splittedMarket[0]

def getSummedMetrics():
    summedMetrics = {}
    if len(metrics) == 0:
        return metrics
    for metric in metrics:
        strategy = metric["strategy"]["module"]
        market = metric["market"]
        inverseMarket = getInverseMarket(market)

        if strategy in summedMetrics:
            foundMarkets = [summedMarket for summedMarket in summedMetrics[strategy]["markets"] if summedMarket["market"] == market]
            foundInverseMarkets = [summedMarket for summedMarket in summedMetrics[strategy]["markets"] if summedMarket["market"] == inverseMarket]
            if len(foundMarkets) > 0:
                print("Market already exists, amount will be added.")
                summedMarket = foundMarkets[0]
                amount = summedMarket["amount"]
                summedMarket["amount"] = metric["amount"] + amount
            elif len(foundInverseMarkets):
                print("Inverse market already exists, amount will be added.")
                summedMarket = foundInverseMarkets[0]
                amount = summedMarket["amount"]
                summedMarket["amount"] = metric["amount"] + amount
            else:
                summedMetrics[strategy]["markets"].append({
                    "market": market,
                    "amount": metric["amount"]
                })
        else:
            summedMetrics[strategy] = {
                "strategy": strategy,
                "markets": [
                    {   
                        "amount": metric["amount"],
                        "market": metric["market"]
                    }
                ]
            }
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


def get_index_of_metric(m):
    inverseMarket = getInverseMarket(m["market"])
    items = [i for i, metric in enumerate(metrics) if m["account_name"] == metric["account_name"] and (metric["market"] == m["market"] or metric["market"] == inverseMarket)]
    if len(items) == 0:
        return -1
    return items[0]
    
def check_if_already_exists(m):
    #metric = [metric for metric in metrics if metric['account_name'] == m['account_name'] 
    #and (metric["market"] == m["market"] or metric["market"] == inverseMarket)]
    #index = [index if m["account_name"] == metric["account_name"] else -1 for index, metric in enumerate(metrics)] 
    #[i if val == x.id else -1 for i,x in enumerate(a)] 
    index = get_index_of_metric(m)
    return index > -1

class AddMetricAPI(Resource):
    def post(self):
        abort_invalid_metric()
        if check_if_already_exists(request.json):
            return "Metric already exists, hence it was updated...", 200
        metric = request.json
        metrics.append(metric)
        return "Metric successfully added.", 201


class RemoveMetricAPI(Resource):
    def post(self):
        abort_invalid_metric()
        index = get_index_of_metric(request.json)
        if index > -1:
            del metrics[index]
            return "Metric successfully removed...", 200
        else:
            return "Metric does not exist.", 204
