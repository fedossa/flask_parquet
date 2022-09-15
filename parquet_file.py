from flask import send_file
from flask_restful import Resource
from user import User


def is_valid(api_key):
    user = User.find_by_api_key(api_key)
    if user is not None:
        return True


class ParquetFile(Resource):
    def get(self, api_key, file_name):
        if is_valid(api_key):
            return send_file(f"static/{file_name}/{file_name}.parquet")
        return {"message": "The provided API key is not valid"}, 403
