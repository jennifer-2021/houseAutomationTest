import json

CONFIG_PATH = "testdata/house_home.json"


def get_home_json():
    config_file = open(CONFIG_PATH)
    home_data = json.load(config_file)
    return home_data


class JsonReader:

    @staticmethod
    def get_home_province_data():
        home_data = get_home_json()
        return home_data["provinces"]

    @staticmethod
    def get_home_city_data():
        home_data = get_home_json()
        return home_data["cities"]