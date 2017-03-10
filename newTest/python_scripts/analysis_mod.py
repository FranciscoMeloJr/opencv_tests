import json
from pprint import pprint

def read():
    with open('/var/www/html/siteTest/data/open1001.json') as data_file:
        data = json.load(data_file)
    return data

def print_executions(data):
    i = 0
    while i < 100:
        print (data["executions"][i]['a'])
        i = i + 1

def main():
    data = read()
    #pprint(data)
    print_executions(data)

main()


#"masks": {       "id": "valore"     },     "om_points": "value",    "parameters": {         "id": "valore"     } }
#data["maps"][0]["id"]
