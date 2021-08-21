import json

CONFIG_PATH = "testdata/new_home.json"


class JsonReader:

    @staticmethod
    def get_search_suggested_cities_data():
        config_file = open(CONFIG_PATH)
        # convert config_file to the json object: newhome_data
        newhome_data = json.load(config_file)
        return newhome_data["suggestedCity"]

    @staticmethod
    def get_search_building_type_data():
        config_file = open(CONFIG_PATH)
        newhome_data = json.load(config_file)
        return newhome_data["buildingType"]

    @staticmethod
    def get_search_checkin_time_data():
        config_file = open(CONFIG_PATH)
        newhome_data = json.load(config_file)
        return newhome_data["checkinTime"]
