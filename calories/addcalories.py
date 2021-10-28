from os import EX_CANTCREAT
import pandas as pd
import json

starbucks_df = pd.read_csv("Starbucks.csv")
calories_df = pd.read_csv("Calories.csv")

calories_dict = {}
for calories_row in calories_df.iterrows():
    try:
        calories_dict[int(calories_row[1]['SKU'])] = str(calories_row[1]['Size']) + ' / ' + str(calories_row[1]['Calories'])
    except:
        pass

nutritional_array = []
for index, row in starbucks_df.iterrows():
    nutritional_string = ''
    if '&' in row['Barcode']:
        skus = row['Barcode'].split('&')
        for sku in skus:
            try:
                sku = int(sku)
                if sku in calories_dict.keys():
                    nutritional_string += calories_dict[sku] + ', '
            except:
                pass
        nutritional_string = nutritional_string[:-2]
    nutritional_array.append(nutritional_string)

starbucks_df['Nutritional Data'] = nutritional_array

starbucks_df.to_csv('output.csv')