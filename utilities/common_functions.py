import json

class Common_functions:

    def __init__(self):
        pass

    def get_test_data(self):
        with open("test_data/test_data.json") as j:
            return json.load(j)