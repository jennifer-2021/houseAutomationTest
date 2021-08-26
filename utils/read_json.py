import json

CONFIG_PATH = "testdata/new_home.json"


def get_newhome_json():
    config_file = open(CONFIG_PATH)
    newhome_data = json.load(config_file)
    return newhome_data


class JsonReader:

    @staticmethod
    def get_search_suggested_cities_data():
        newhome_data = get_newhome_json()
        return newhome_data["suggestedCity"]

    @staticmethod
    def get_filter_building_type_data():
        newhome_data = get_newhome_json()
        return newhome_data["buildingType"]

    @staticmethod
    def get_filter_checkin_time_data():
        newhome_data = get_newhome_json()
        return newhome_data["checkinTime"]

    @staticmethod
    def get_filter_min_price_data():
        newhome_data = get_newhome_json()
        return newhome_data["minPrice"]

    @staticmethod
    def get_search_city_with_filters():
        newhome_data = get_newhome_json()
        return newhome_data["cityWithFilters"]

    @staticmethod
    def get_address_data():
        newhome_data = get_newhome_json()
        return newhome_data["address"]

    @staticmethod
    def get_real_estate_data():
        newhome_data = get_newhome_json()
        return newhome_data["realEstate"]

    @staticmethod
    def get_developer_data():
        newhome_data = get_newhome_json()
        return newhome_data["developer"]

    @staticmethod
    def get_tags_data():
        newhome_data = get_newhome_json()
        return newhome_data["tagsOnImage"]

    @staticmethod
    def get_mapPoint_data():
        newhome_data = get_newhome_json()
        return newhome_data["mapPoints"]