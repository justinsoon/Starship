import pandas as pd
import json

df = pd.read_csv('finalAdded.csv', usecols= ['Name', 'Price', 'Modifiers'])
array = []
name = ''
price = 0

# Finding matches and updating values
def modifierRow():
    for index, row in df.iterrows():
        name = row['Name']
        try:
            row['Modifiers'] = json.loads(row['Modifiers'])
        except:
            row['Modifiers'] = []
        for item in json.loads(json.dumps(row['Modifiers'])):
            for value in item['values']:
                if (value['title'] == name):
                    value['price'] = round(float(price)) * 100
    df.to_csv('test.csv')

modifierRow()