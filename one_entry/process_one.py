import json


data = None
id = "B00E6FGSHY"
with open("one_entry.json",'r') as file:
    data = json.load(file)[id]

all_tags = set(data['positive'] + data['negative'])

tags = {}

for i in all_tags:
    tags[i] = {'category': ''}


with open("one_entry_keywords.json",'w') as file:
    json.dump(tags,file)