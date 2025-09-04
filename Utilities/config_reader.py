import json
import os

class ConfigReader:
    def __init__(self, config_file="config/config.json"):
        self.config_file = config_file
        with open(self.config_file, "r") as f:
            self.config = json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)
