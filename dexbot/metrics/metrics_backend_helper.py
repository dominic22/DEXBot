import requests 
import json

def getIdFromMetric(metric):
    return metric.account_name + '_' + metric.base_asset + '_' + metric.quote_asset

def send_metric():
    metric = {
        'id':'dominic-test_DEXBOT1_DEXBOT2',
        'chain_id': '1',
        'signature': '',
        'account_name' : 'Dominic-Test121',
        'base_asset' : 'DEXBOT1',
        'quote_asset' : 'DEXBOT2',
        'order_size': 200,
        'strategy' : {
            'strat': 'dexbot.strategies.staggered_orders',
            'mode': 1,
        },
    }
    headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    requests.post('http://localhost:5000/add_metric', json=metric, headers=headers)


def addWorkerMetric(worker, config):
    print("JSON STRAT " + json.dumps(config))
    print("11worker worker_name " + worker['market'])
    print("11worker account " + worker['account'])
    print("11worker amount: " + str(worker["amount"]))

    headers = {'Content-type': 'application/json', 'Accept': '*/*'}

    if(worker['module'] == 'dexbot.strategies.relative_orders'):
        strategy = {
            'module': 'dexbot.strategies.staggered_orders',
            'mode': 1,
        }
    else:
        strategy = {
            'module': 'dexbot.strategies.relative_orders',
        }
    id = worker['account'] + "_" + worker['market']
    workerReq = {
        'id': id,
        'chain_id': '1',
        'signature': '',
        'account_name' : worker['account'],
        'market' : worker['market'],
        'order_size' : str(worker["amount"]),
        'strategy' : strategy,
    }
    print("Sending worker to metrics backend...")
    requests.post('https://enjf31b1lqkkq.x.pipedream.net', json=workerReq, headers=headers)
    