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

    @staticmethod
    def get_price_data():
        mls_data = get_mls_json()
        return mls_data["price"]

    @staticmethod
    def get_bedroom_data():
        mls_data = get_mls_json()
        return mls_data["bedroom"]

    @staticmethod
    def get_days_on_market_data():
        mls_data = get_mls_json()
        return mls_data["daysOnMarket"]

    @staticmethod
    def get_area():
        mls_data = get_mls_json()
        return mls_data["area"]

    @staticmethod
    def get_parking_lot():
        mls_data = get_mls_json()
        return mls_data["parking"]

    @staticmethod
    def get_sorting():
        mls_data = get_mls_json()
        return mls_data["sorting"]

    @staticmethod
    def get_transaction_on_map():
        mls_data = get_mls_json()
        return mls_data["transactionsOnMap"]

    @staticmethod
    def get_school_grade_map():
        mls_data = get_mls_json()
        return mls_data["schoolGrade"]

    @staticmethod
    def get_school_rank_map():
        mls_data = get_mls_json()
        return mls_data["schoolRank"]

    @staticmethod
    def get_modal_link():
        mls_data = get_mls_json()
        return mls_data["modals"]