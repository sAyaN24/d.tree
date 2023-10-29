import json

# data = None

# with open('result_pn.json','r') as file:
#     data = json.load(file)

# keywords = []

# for model in data:
#     keywords += data[model]['positive']
#     keywords += data[model]['negative']

# keywords_defined = [

# ]

# stats = {}


# keywords = set(keywords)

# count = 0



# for i in keywords_defined:
#     for j in keywords:
#         if(i.lower() in j.lower()):
#             count += 1

# print(count)

# for i in keywords:
#     stats[i] = {
#         "category" : ""
#     }


# with open("keywords.txt" , 'w',encoding="utf-8") as file:
#     json.dump(stats,file)


#     "Quality",
#     "Display" ,
#     "Camera" ,
#     "batery" ,
#     "Processor",
#     "Signal Strength",
#     "Connectivity",
#     "Customer Service",
#     "Charger",
#     "Speaker",
#     "appearance",
#     "Delivery",
#     "Case Provided",
#     "keyboard",
#     "UI",
#     "screen", "size", "color", "picture",
#     "Connection",
#     "SIM",
#     "service",
#     "Sound",
#     "look",
#     "deliver","arrived",
#     "case",
#     "button",
#     "menu" , "UI"


keywords = None

with open("keywords.json",'r') as file:
    keywords = json.load(file)

print(f'total count : {len(keywords.keys())}')
cnt = 0
for i in keywords:
    if(keywords[i]["category"] == ""):
        cnt += 1
print(f'still empty : {cnt}')

word = "process"
replace_word = "PROCESSOR"
count = 0

for i in keywords:
    if(keywords[i]["category"] == ""):
        if(word.lower() in i.lower()):
            keywords[i]["category"] = replace_word
            count+= 1
        if(len(i) <= 2):
            keywords[i]["category"] = "NA"
            count+=1

print(f'filled this attempt: {count}')

with open("keywords.json" , 'w',encoding="utf-8") as file:
    json.dump(keywords,file)