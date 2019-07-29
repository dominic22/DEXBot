from flask import Flask
from flask_restful import Api

# I would have expected to import from: metrics_backend.metrics_api but it doesn't work, do you know why?
from metrics_api import MetricsAPI, AddMetricAPI, MetricAPI, StatisticsAPI, RemoveMetricAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(MetricsAPI, '/metrics')
api.add_resource(StatisticsAPI, '/statistics')
api.add_resource(MetricAPI, '/metrics/<string:id>')
api.add_resource(AddMetricAPI, '/add_metric')
api.add_resource(RemoveMetricAPI, '/remove_metric')

if __name__ == '__main__':
    app.run(debug=True)
