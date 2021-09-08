import json

CONFIG_PATH = "testdata/mls.json"


def get_mls_json():
    config_file = open(CONFIG_PATH)
    mls_data = json.load(config_file)
    return mls_data


class JsonReader:

    @staticmethod
    def get_mls_suggested_cities_data():
        mls_data = get_mls_json()
        return mls_data["suggestCity"]

    @staticmethod
    def get_search_by_mls_data():
        mls_data = get_mls_json()
        return mls_data["searchByMls"]

    @staticmethod
    def get_mls_search_data():
        mls_data = get_mls_json()
        return mls_data["searchKey"]

    @staticmethod
    def get_transaction_status_data():
        mls_data = get_mls_json()
        return mls_data["transactionStatus"]

    @staticmethod
    def get_transaction2_status_data():
        mls_data = get_mls_json()
        return mls_data["transactionStatus2"]

    @staticmethod
    def get_building_type_data():
        mls_data = get_mls_json()
        return mls_data["buildingType"]