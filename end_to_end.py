import datetime
import json

import re
from datetime import date

from utils.test_utils import TestUtils


class TestOne():

    def test_convertion(self):
        t = ["10", "12", "22"]
        for i in t:
            print(i)
            if i == "10":
                continue








    def atest_url(self):
        url = "https://house.51.ca/mls?buildingType=2%2C3&region=44.20128885967054%2C-79.89050315188348%2C43.41440746065908%2C-78.97863791750851&transactionType=1&limit=200"
        url = "https://house.51.ca/mls?region=44.17568615978678%2C-79.86921714114095%2C43.44033849670947%2C-78.99992392825044&transactionType=1&limit=200"
        url = "https://house.51.ca/mls?region=44.17568615978678%2C-79.86921714114095%2C43.44033849670947%2C-78.99992392825044&transactionType=1&limit=200"
        region = {}
        content = url.split("?")[1]
        contents = content.split("&")
        for c in contents:
            ary = c.split("=")
            key = ary[0]
            value = ary[1].replace("%2C%20", " ")
            value = value.replace("%20", " ")
            if key == "buildingType":
                value = value.replace("%2C", ",")
            if key != "region":
                region[key] = value

        print(str(region))
        s = str(region)
        print(type(region))
        print(type(s))
        print(s == str(region))
        d = json.dumps(region)
        print(type(d))
