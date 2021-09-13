import json

CONFIG_PATH = "testdata/rental.json"


def get_rental_json():
    config_file = open(CONFIG_PATH)
    rental_data = json.load(config_file)
    return rental_data


class JsonReader:

    @staticmethod
    def get_province_data():
        rental_data = get_rental_json()
        return rental_data["province"]

    @staticmethod
    def get_city_data():
        rental_data = get_rental_json()
        return rental_data["cities"]