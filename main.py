from json import load,dump
import pandas as pd

df = pd.read_csv("dataset.csv")

data = None

with open("analysis_result.json",'r') as file:
    data = load(file)




result = {}

for i,element in enumerate(data):
    id = df.loc[[i]]['asin'].item()
    if(id not in result):
        result[id] = { 'positive': [] ,'negative': []}
    for i in range(len(element['aspect'])):
        if(element['sentiment'][i] == 'Positive'):
            result[id]['positive'].append(element['aspect'][i])
        else:
            result[id]['negative'].append(element['aspect'][i])


print(len(result.keys()))

with open('result_pn.json','w') as file:
    dump(result,file)



