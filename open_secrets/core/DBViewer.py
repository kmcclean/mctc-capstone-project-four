from open_secrets.core.DBController import DBController
from urllib import request
import json

class DBViewer:

    def __init__(self):
        controller = DBController()
        self.controller = controller

    def search(self):
        search_name = input("Please input the name you wish to search: ")
        results = self.controller.db_search(search_name)
        return results

    def close(self):
        self.controller.db_close()

    def get_key(self, key_name):
        f = open('keys.txt', 'r')
        for line in f:
            if key_name in line:
                key_list = line.split(":")
                key = key_list[1]
                key = key.strip()
                return key

    def get_open_secrets(self):
        search_results = self.search()
        api_key = self.get_key("Open_Secrets_API_KEY_2")
        results_list = []
        for item in search_results:
            url = "http://www.opensecrets.org/api/?method=candContrib&cid=" + item[0] + "&cycle=2016&apikey=" + api_key +  "&output=json"
            print(url)
            open_secrets_results = request.urlopen(url)
            results_list.append(open_secrets_results)

        return results_list

    def output_open_secrets_results(self, results):

        try:
            for candidate in results:
                jsonInfo = json.loads(candidate.readall().decode('utf-8'))
                json_level_one = jsonInfo["response"]
                json_level_two = json_level_one["contributors"]
                json_level_three = json_level_two["@attributes"]
                for item in json_level_three:
                    print(item)

        except Exception as e:
            print("Error in output_open_secrets_results: " + e)


view = DBViewer()
top_results = view.get_open_secrets()
view.output_open_secrets_results(top_results)
view.close()
