from flask import Flask
from flask_restful import Api

from parquet_file import ParquetFile

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'some_secret_key'
api = Api(app)

api.add_resource(ParquetFile, '/<string:api_key>/<string:file_name>')
