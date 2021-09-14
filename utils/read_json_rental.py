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

    @staticmethod
    def get_catalog_data():
        rental_data = get_rental_json()
        return rental_data["catalogs"]

    @staticmethod
    def get_subway_data():
        rental_data = get_rental_json()
        return rental_data["subway"]

    @staticmethod
    def get_university_data():
        rental_data = get_rental_json()
        return rental_data["university"]

    @staticmethod
    def get_buildingType_data():
        rental_data = get_rental_json()
        return rental_data["buildingTypes"]

    @staticmethod
    def get_publish_links_data():
        rental_data = get_rental_json()
        return rental_data["publishlinks"]

    @staticmethod
    def get_rental_links_data():
        rental_data = get_rental_json()
        return rental_data["rentallinks"]