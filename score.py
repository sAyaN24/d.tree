import json
from math import floor

product_review = None
reviews = None

with open("one_entry.json","r") as file:
    product_review = json.load(file)

with open("one_entry_keywords.json",'r') as file:
    reviews = json.load(file)

keywords = set([reviews[elm]['category'] for elm in reviews])

result = {}

for key in keywords:
    if(key != 'NA'):
        result[key] = {'positive': 0,'negative': 0}

id = "B00E6FGSHY"

for i in product_review[id]['positive']:
    if(reviews[i]['category'] != "NA"):
        result[reviews[i]['category']]['positive'] += 1

for i in product_review[id]['negative']:
    if(reviews[i]['category'] != "NA"):
        result[reviews[i]['category']]['negative'] += 1

with open("one_entry_analysis.json",'w') as file:
    json.dump(result,file)


rating = {}
rating['id'] = id

for i in result:
    total_count = result[i]['positive'] + result[i]['negative']
    rating[i] = floor((result[i]['positive'] / total_count) * 10)

with open('one_entry_rating.json','w') as file:
    json.dump(rating,file)