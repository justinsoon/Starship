import pandas as pd
import numpy as np
import json

df = pd.read_csv('finalAdded.csv', usecols= ['Name', 'Price', 'Modifiers'])
array = []
name = df['Name'].to_numpy()

# Finding matches and updating values
def modifierRow():
    for index, row in df.iterrows():
        try:
            row['Modifiers'] = json.loads(row['Modifiers'])
        except:
            row['Modifiers'] = []
        for item in json.loads(json.dumps(row['Modifiers'])):
            for value in item['values']:
                if value['title'] in name:
                    for x in name:
                        if  value['title'] == x:
                            tempName = row['Name']
                            priceRow = df.loc[df.Name == tempName, 'Price'].values[0]
                            value['price'] = round(float(priceRow)) * 100
    df.to_csv('test.csv')

modifierRow()
