from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api
from metrics import MetricsAPI, AddMetricAPI, MetricAPI, StatisticsAPI

app = Flask(__name__)
api = Api(app)



'''
@app.route('/')
def index():
    return "Hello, World!" + __name__

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 4)
'''

api.add_resource(MetricsAPI, '/metrics')
api.add_resource(StatisticsAPI, '/statistics')
api.add_resource(MetricAPI, '/metrics/<string:id>')
api.add_resource(AddMetricAPI, '/add_metric')

if __name__ == '__main__':
    app.run(debug=True)