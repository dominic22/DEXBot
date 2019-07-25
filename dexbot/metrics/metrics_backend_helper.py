import requests 
import json

#url = "https://enjf31b1lqkkq.x.pipedream.net"
url = "http://localhost:5000"

def addWorkerMetric(worker, config):
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
    workerReq = {
        'chain_id': '1',
        'signature': '',
        'account_name' : worker['account'],
        'market' : worker['market'],
        'amount' : str(worker["amount"]),
        'strategy' : strategy,
    }
    print("Sending worker to metrics backend...")
    requests.post(url + "/add_metric", json=workerReq, headers=headers)
    