import json

my_json={   "car":"dacia","age":16,
            "functional":False,"attributes":[
                {"capacity":1190},
                {"power":100},
                {"model":"logan"}
                ]}

with open('json_written.json','wt') as f:
    json.dump(my_json,f,indent=4)
