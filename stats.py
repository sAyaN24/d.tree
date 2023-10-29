import json

data = None


with open("analysis_result.json",'r') as file:
    data = json.load(file)

print(len(data))
# empty_entry = 0

# n = 50
# first_n = data

# for i in range(67965):
#     print(data[i]['sentence'][0:5])