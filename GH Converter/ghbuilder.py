import pandas as pd
import json
import random
import math

def get2DigitHex(value):
    result = ''
    hexRef = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    remainder = value % 16
    mod = math.floor(value /16)
    result += hexRef[mod]
    result += hexRef[remainder]
    return result

class Modifier:
    
    def __init__(self, _id, title, description, type, image, sort_order, disabled,
                 values, price_increase_applicable, max_selected_values,
                 max_qty_sum, default_value, preselect_default_value):
        self._id = _id
        self.title = title
        self.description = description
        self.type = type
        self.image = image
        self.sort_order = sort_order
        self.disabled = disabled
        self.values = values
        self.price_increase_applicable = price_increase_applicable
        self.max_selected_values = max_selected_values
        self.max_qty_sum = max_qty_sum
        self.default_value = default_value
        self.preselect_default_value = preselect_default_value

    def __str__(self):
        return json.dumps(self.__dict__)

class Value:
    
    def __init__(self, _id, title, price, sort_order, price_increase_type, 
            price_increase_amount, default_qty, max_qty):
    
        self._id = _id
        self.title = title
    
        # Price is in pennies. (so $1.00 would be 100)
    
        self.price = price
    
        # Index
    
        self.sort_order = sort_order
        self.price_increase_type = price_increase_type
        self.price_increase_amount = price_increase_amount
        self.default_qty = default_qty
        self.max_qty = max_qty
        
    def __str__(self):
        return json.dumps(self.__dict__)

# Variables for variations.

_id = "UNIMPORTANT"
title = "ToDo"
description = ""
type = "UNIMPORTANT FOR NOW"
image = ""
sort_order = 0
disabled = False
values = []
price_increase_applicable = False

# 1 is default, but should be number = # of add ons, or size of values.

max_selected_values = int(1)
max_qty_sum = None
default_value = {}
default_value["_id"] = "UNIMPORTANT"
preselect_default_value = None

# Variables for items

grubhub_menu = pd.read_csv("Grub Hub Menu.csv", encoding='latin1')

Global_ID = ""
Barcode = ""
Name = "ToDo"
Status = ""
Unit = ""
Number_of_units = ""
Units_per_pack = ""
Categories = "ToDo"
Price = ""
Price_with_markup = "" 
Price_with_commission = ""
Price_base = ""
Markup = ""
Commission = ""
Location_in_store = ""
Location_priority = -1
Preparation_time = ""
Tax_code = "General"
Freetext_notes = ""
Item_taxes = ""
Filters = []
Description = ""
Allergen_Information = ""
Ingredients = ""
Nutritional_data = ""
Dietary_information = ""
Station = ""
Modifiers = []
Private = "no"
Tags = ""

starship_csv = pd.read_csv("Starship.csv")

# modifier = Modifier(Id, title, description, type, image, sort_order,
#                     disabled, values, price_increase_applicable,
#                     max_selected_values, max_qty_sum, default_value,
#                     preselect_default_value)

starship_csv = pd.DataFrame(columns=starship_csv.columns)

values = {}
Modifiers = {}

variation_index = 0
value_index = 0

Modifier_array = []

for index, row in grubhub_menu.iterrows():
    
    if not pd.isna(row["Category"]):
        
        if Categories == "ToDo":
            
            Categories = row['Category']
            Location_in_store = Categories
            Name = row['Item']
            Description = row['Item Description']
            Global_ID = row['Barcode']
            Barcode = row['Barcode']
            Price = row['Item Base Price']
            Price_with_commission = Price
            Price_with_markup = Price
            Price_base = row['Item Base Price']
            Nutritional_Data = str(row['Calories']) + " Calories"
            
        else:
            
            Modifier_array = [0] * len(Modifiers)
            
            for key, value in Modifiers.items():
                
                value = value.replace('\"false\"', "false")
                value = value.replace('\"true\"', "true")
                
                Modifier_array[key] = json.loads(value)
            
            starship_csv = starship_csv.append(
                pd.DataFrame(
                    [[Global_ID,
                      Barcode,
                      Name,
                      Status,
                      Unit,
                      Number_of_units,
                      Units_per_pack,
                      Categories,
                      Price,
                      Price_with_markup,
                      Price_with_commission,
                      Price_base,
                      Markup,
                      Commission,
                      Location_in_store,
                      Location_priority,
                      Preparation_time,
                      Tax_code,
                      Freetext_notes,
                      Item_taxes,
                      Filters,
                      Description,
                      Allergen_Information,
                      Ingredients,
                      Nutritional_data,
                      Dietary_information,
                      Station,
                      json.dumps(Modifier_array),
                      Private,
                      Tags
                      ]], columns=starship_csv.columns))
            
            Categories = row['Category']
            Location_in_store = Categories
            Name = row['Item']
            Description = row['Item Description']
            Global_ID = row['Barcode']
            Barcode = row['Barcode']
            Price = row['Item Base Price']
            Price_with_commission = Price
            Price_with_markup = Price
            Price_base = row['Item Base Price']
            Nutritional_Data = str(row['Calories']) + " Calories"
            
            Modifiers = {}
            
            variation_index = 0
            
    elif not pd.isna(row['Item']):
        
        if Name == "ToDo":
            
            Name = row['Item']
            Description = row['Item Description']
            Global_ID = row['Barcode']
            Barcode = row['Barcode']
            Price = row['Item Base Price']
            Price_with_commission = Price
            Price_with_markup = Price
            Price_base = row['Item Base Price']
            Nutritional_Data = str(row['Calories']) + " Calories"
            
        else:
            
            Modifier_array = [0] * len(Modifiers)
            
            for key, value in Modifiers.items():
                
                value = value.replace('\"false\"', "false")
                value = value.replace('\"true\"', "true")
                
                Modifier_array[key] = json.loads(value)
            
            starship_csv = starship_csv.append(
                pd.DataFrame(
                    [[Global_ID,
                      Barcode,
                      Name,
                      Status,
                      Unit,
                      Number_of_units,
                      Units_per_pack,
                      Categories,
                      Price,
                      Price_with_markup,
                      Price_with_commission,
                      Price_base,
                      Markup,
                      Commission,
                      Location_in_store,
                      Location_priority,
                      Preparation_time,
                      Tax_code,
                      Freetext_notes,
                      Item_taxes,
                      Filters,
                      Description,
                      Allergen_Information,
                      Ingredients,
                      Nutritional_data,
                      Dietary_information,
                      Station,
                      json.dumps(Modifier_array),
                      Private,
                      Tags
                      ]], columns=starship_csv.columns))
            
            Name = row['Item']
            Description = row['Item Description']
            Global_ID = row['Barcode']
            Barcode = row['Barcode']
            Price = row['Item Base Price']
            Price_with_commission = Price
            Price_with_markup = Price
            Price_base = row['Item Base Price']
            Nutritional_Data = str(row['Calories']) + " Calories"
            
            Modifiers = {}
            
            variation_index = 0
            
    elif not pd.isna(row['Group']):
        
            value_index = 0

            hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
            generated_list = random.choices(hex_list, k=22)
            hexNumber = ''
            for item in generated_list:
                hexNumber += item
            firstHex = hexNumber + '00'

            _id = firstHex
            title = row['Group']
            description = ""
            type = "LATER"
            image = "https://starship-vending.s3.eu-west-1.amazonaws.com/modifier-604a56aa6ea3c917d310041c-1625519978130.png"
            sort_order = variation_index
            disabled = "false"
            
            choices = str(row['Modifiers']).split(", ")
            price = ""
                
            array = [0] * len(choices)
            
            for item in choices:
                
                price = 0
                
                item_array = item.split("(+")
                
                item = item_array[0].strip()

                valueId = hexNumber + get2DigitHex(value_index + 1)
                
                if not pd.isna(row['Max']):
                    if len(choices) < int(row['Max']):
                        max_qty = len(choices)
                    else:
                        max_qty = int(row['Max'])
                else:
                    max_qty = len(choices)
                    
                if len(item_array) == 2:
                
                    price = ""
                
                    for letter in item_array[1]:
                    
                        if letter.isnumeric():
                    
                            price += str(letter)
                
                values[value_index] = json.loads(Value(valueId, item, int(price), value_index, None, None, 1, max_qty).__str__())
                array[value_index] = values[value_index]
                value_index += 1
                
            max_increase_applicable = "false"
            
            if not pd.isna(row['Max']):
               
                if len(choices) < int(row['Max']):
                    max_selected_values = len(choices)
                else:
                    max_selected_values = int(row['Max'])
                
                if int(row['Max']) == 1:
                    
                    if not pd.isna(row['Min']): 
                        
                        if int(row['Min']) == 1:
                            
                            type = 10
                        
                        else:
                            
                            type = 30

                    else:
                        
                        type = 30
                        
                else:
                    
                    type = 30
                
            else:
                
                max_selected_values = len(choices)
                type = 30
                
            max_qty_sum = None
            
            # Default_value set earlier
        
            defaultValueId = hexNumber + '01'

            default_value = {"_id": defaultValueId}

            preselect_default_value = "false"
            
            Modifiers[variation_index] = str(json.dumps(json.loads(Modifier(_id, title, description,
                                                 type, image, sort_order,
                                                 disabled, array,
                                                 price_increase_applicable,
                                                 max_selected_values,
                                                 max_qty_sum,
                                                 default_value,
                                                 preselect_default_value).__str__())))
            
            variation_index += 1

Modifier_array = [0] * len(Modifiers)
            
for key, value in Modifiers.items():
    
    value = value.replace('\"false\"', "false")
    value = value.replace('\"true\"', "true")
    
    Modifier_array[key] = json.loads(value)

starship_csv = starship_csv.append(
                pd.DataFrame(
                    [[Global_ID,
                      Barcode,
                      Name,
                      Status,
                      Unit,
                      Number_of_units,
                      Units_per_pack,
                      Categories,
                      Price,
                      Price_with_markup,
                      Price_with_commission,
                      Price_base,
                      Markup,
                      Commission,
                      Location_in_store,
                      Location_priority,
                      Preparation_time,
                      Tax_code,
                      Freetext_notes,
                      Item_taxes,
                      Filters,
                      Description,
                      Allergen_Information,
                      Ingredients,
                      Nutritional_data,
                      Dietary_information,
                      Station,
                      json.dumps(Modifier_array),
                      Private,
                      Tags
                      ]], columns=starship_csv.columns))

for i, col in enumerate(starship_csv.columns):
    starship_csv.iloc[:, i] = starship_csv.iloc[:, i].astype(str).str.replace("\[\'\{","[{")
    starship_csv.iloc[:, i] = starship_csv.iloc[:, i].astype(str).str.replace("\}\'\]","}]")

starship_csv.to_csv('Final.csv', index=False)