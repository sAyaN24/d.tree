import pandas as pd
import random
from json import dump

def readDataset(path):
    return pd.read_csv(path)

def template(df_entry):
    return {
        'id' : df_entry['asin'],
        'brand': df_entry['brand'],
        'title': df_entry['title'],
        'url': df_entry['url'],
        'image':df_entry['image'],
        'rating':df_entry['rating'],
        'reviewUrl':df_entry['reviewUrl'],
        'totalReview':int(df_entry['totalReviews']),
        'price':df_entry['price'],
        'originalPrice':df_entry['originalPrice'],
        'SECURITY': random.randint(0,10),
        'VFM': random.randint(0,10),
        'KEYBOARD': random.randint(0,10),
        'CONNECTIVITY': random.randint(0,10),
        'LOOK': random.randint(0,10),
        'DISPLAY': random.randint(0,10),
        'OS': random.randint(0,10),
        'ACCESSORIES': random.randint(0,10),
        'AUDIO': random.randint(0,10),
        'SERVICE': random.randint(0,10),
        'CAMERA': random.randint(0,10),
        'BATTERY': random.randint(0,10),
        'STORAGE': random.randint(0,10),
        'SOFTWARE': random.randint(0,10),
        'CHARGER': random.randint(0,10),
        'VENDOR_SERVICE': random.randint(0,10),
        'RAM': random.randint(0,10),
        'MANUAL': random.randint(0,10),
        'HARDWARE': random.randint(0,10)
    }


data = readDataset("product_list.csv")

# print(template(data.iloc[0]))
words = ['SECURITY', 'VFM', 'KEYBOARD', 'CONNECTIVITY', 'LOOK', 'DISPLAY', 'OS', 'ACCESSORIES', 'AUDIO', 'SERVICE', 'CAMERA', 'BATTERY', 'STORAGE', 'SOFTWARE', 'CHARGER', 'VENDOR_SERVICE', 'RAM', 'MANUAL', 'HARDWARE']
all_product = []

for i in range(data.shape[0]):
    temp = template(data.iloc[i])
    total = 0
    for i in words:
        total += temp[i]
    temp['overall_rating'] = round(total / len(words),1)
    all_product.append(temp)

print(all_product[0]['id'])

all_product = sorted(all_product,key=lambda i: i['overall_rating'])

print(all_product[0]['id'])

with open('product_db.json','w') as file:
    dump(all_product,file)


