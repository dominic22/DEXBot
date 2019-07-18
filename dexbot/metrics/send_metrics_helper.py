import requests 

def send_metric():
    metric = {
        "chain_id": "1",
        "signature": "",
        "account_name" : "Dominic-Test121",
        "strategy" : {
            "strat": "dexbot.strategies.staggered_orders",
            "base_asset" : "DEXBOT1",
            "quote_asset" : "DEXBOT2",
            "mode": 1,
            "order_size": 200,
        },
    }
    headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    requests.post('http://localhost:5000/add_metric', json=metric, headers=headers)

send_metric()