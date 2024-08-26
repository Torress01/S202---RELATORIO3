import json
import os
from datetime import datetime

from bson import json_util


class Pokedex:
    def __init__(self, db):
        self.db = db

    @staticmethod
    def write_a_json(data):
        parsed_json = json.loads(json_util.dumps(data))

        if not os.path.isdir("./logs"):
            os.makedirs("./logs")

        log_file_path = "./logs/logs.json"

        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        existing_data.append(parsed_json)

        with open(log_file_path, 'w') as f:
            json.dump(existing_data, f,
                      indent=4,
                      separators=(',', ': ')
                      )

    def get_pokemon_by_name(self, name: str):
        query = {"name": name}
        result = self.db.collection.find(query)
        log_data = {
            "function": "get_pokemon_by_name",
            "query": query,
            "result": list(result),
        }
        self.write_a_json(log_data)
        return result

    def get_pokemon_by_type(self, pokemon_type: str):
        query = {"type": pokemon_type}
        result = self.db.collection.find(query)
        log_data = {
            "function": "get_pokemon_by_type",
            "query": query,
            "result": list(result),
        }
        self.write_a_json(log_data)
        return result

    def get_pokemon_by_weakness(self, weakness: str):
        query = {"weaknesses": weakness}
        result = self.db.collection.find(query)
        log_data = {
            "function": "get_pokemon_by_weakness",
            "query": query,
            "result": list(result),
        }
        self.write_a_json(log_data)
        return result

    def get_pokemon_by_id(self, pokemon_id: int):
        query = {"id": pokemon_id}
        result = self.db.collection.find(query)
        log_data = {
            "function": "get_pokemon_by_id",
            "query": query,
            "result": list(result),
        }
        self.write_a_json(log_data)
        return result

    def get_pokemon_by_num(self, num: str):
        query = {"num": num}
        result = self.db.collection.find(query)
        log_data = {
            "function": "get_pokemon_by_num",
            "query": query,
            "result": list(result),
        }
        self.write_a_json(log_data)
        return result
