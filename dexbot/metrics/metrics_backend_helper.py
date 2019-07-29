import requests

# url = "https://enjf31b1lqkkq.x.pipedream.net"
url = "http://localhost:5000"


def add_worker_metric(worker):
    headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    if worker['module'] == 'dexbot.strategies.relative_orders':
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
        'account_name': worker['account'],
        'market': worker['market'],
        'amount': worker["amount"],
        'strategy': strategy,
    }
    print("Sending worker to metrics backend...")
    requests.post(url + "/add_metric", json=workerReq, headers=headers)


def remove_worker_metric(worker):
    headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    if worker['module'] == 'dexbot.strategies.relative_orders':
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
        'account_name': worker['account'],
        'market': worker['market'],
        'amount': worker["amount"],
        'strategy': strategy,
    }
    print("Sending worker to metrics backend...")
    requests.post(url + "/remove_metric", json=workerReq, headers=headers)
