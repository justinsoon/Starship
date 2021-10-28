import pandas as pd
import json
import csv

df = pd.read_csv('csv.csv')
array = []
modtype = {10: 'Variation', 20: 'Master Variation', 30: 'Add on', 50: 'Toggle'}

for index, row in df.iterrows():
    try:
        row['Modifiers'] = json.loads(row['Modifiers'])
        
    except:
        row['Modifiers'] = []
    string = ''
    for item in json.loads(json.dumps(row['Modifiers'])):
        string3 = ''
        if item['type'] == 30:
            string3 = ' [Max: ' + str(item['max_selected_values']) + ']'
        string += item['title'] + ' (' + modtype[item['type']] + string3 + '): '
        string2 = ''
        for value in item['values']:
            price = str(float(value['price']) /100)
            if len(price) <4:
                price += '0'
            string2 += value['title'] + ' (+$' + price + "), "
        string += string2
        string += '\n'
    array.append(string)

df['Customization'] = array
df.to_csv('test.csv')