import pandas as pd
import numpy as np
import io
import time
start_time = time.time()
################ Class Objects
class GlobalProduct:
    itemName = ''
    info = ''
    def __init__(self, itemName, globalID):
        self.itemName = itemName
        self.info = globalID
class BarcodeProduct:
    itemName = ''
    info = 0
    def __init__(self, itemName, barCode):
        self.itemName = itemName
        self.info =  (barCode)
class CalProduct:
    itemName = ''
    info = ('', 0)
    def __init__(self, itemName, size, calories):
        self.itemName = itemName
        self.info =  (size, calories)
class PriceProduct:
    itemName = ''
    info = 0
    def __init__(self, itemName, price):
        self.itemName = itemName
        self.info = price
        
################ Functions
######## Basic Reader
def readCSV(fileName, rowSkip):
    fileReader = open(fileName, "r", encoding='UTF-8')
    for i in range(rowSkip):
        fileReader.readline()
    fileContent = fileReader.read()
    return fileContent
######## Store into its respective dictionary
def dictStore(productArray, productDict):
    for product in productArray:
        if product.itemName in (productDict):
            productDict[product.itemName].append(product.info)
        else:
            productDict[product.itemName] = [product.info]
######## Merge two DFs
def normMerge(firstDF, lastDF):
    merge = firstDF.merge(lastDF, on='Name', how='right', suffixes=('', '_y'))
    merge.drop(merge.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
    return merge

################ Variables
bevProducts = []
modProducts = []
foodProducts = []
barcodeProdDict = {}
globalProducts = []
globalProdDict = {}
caloriesProducts = []
priceProducts = []
priceProdDict = {}
calProdDict = {}
removeSizes = ["Kids", "Short", "Tall", "Grande", "Venti", "Trenta"]
removeType = ['Add', 'Extra', 'Light', 'Substitute','Sub', 'No ', ' add', ' extra', ' light', ' sub', ' regular', ' no', 
    ' Modifier', ' Single', ' Double', ' Triple', 'Quad', 'Solo ', 'Doppio ', 'Triple ', ' modifier', ' modifier extra',
    ' modifier light', ' modifier no', ' modifier regular', ' modifier sub', 'Extra ', 'Light ', 'Add ']

#################################### Reading CSVs ####################################
globalContent = readCSV('CSVData/Master.csv', 1)    # Global ID - skip first row
bevContent = readCSV('CSVData/BevSKU.csv', 6)       # Beverages SKU - skip first six row
modContent = readCSV('CSVData/ModSKU.csv', 6)       # Modifier SKU - skip first six row
foodContent = readCSV('CSVData/FoodSKU.csv', 2)     # Food SKU- skip first two row
calContent = readCSV('CSVData/Calories.csv', 1)     # Calories Info - skip first row
priceContent = readCSV('CSVData/Master.csv', 1)     # Prices Info - skip first row

################ Storing Data
######## Global IDs       
for globalLine in globalContent.split('\"\n\"'):
    globalColumns = globalLine.split(',')
    if len(globalColumns) > 4:
        globalName = globalColumns[2]
        globalID = globalColumns[0]
        globalID = globalID.replace('\"', '')
        globalProducts.append(GlobalProduct(globalName, globalID))
dictStore(globalProducts, globalProdDict)
######## Prices
for priceLine in priceContent.split('\"\n\"'):
    priceColumns = priceLine.split(',')
    if len(priceColumns) > 8:
        priceName = priceColumns[2]
        priceItem = priceColumns[8]
        priceProducts.append(PriceProduct(priceName, priceItem))
dictStore(priceProducts, priceProdDict)
######## Beverages 
for bevLine in bevContent.split("\n"):
    bevColumns = bevLine.split(",")
    if len(bevColumns) > 2:
        bevName = bevColumns[1]
        for size in removeSizes:
            bevName = bevName.replace(size, '').strip()
        for type in removeType:
            bevName = bevName.replace(type, '').strip()
        bevBarcode = bevColumns[0]
        bevProducts.append(BarcodeProduct(bevName, bevBarcode))
dictStore(bevProducts, barcodeProdDict)
######## Modifiers
for modLine in modContent.split("\n"):
    modColumns = modLine.split(",")
    if len(modColumns) > 2:
        modName = modColumns[1]
        for size in removeSizes:
            modName = modName.replace(size, '').strip()
        for type in removeType:
            modName = modName.replace(type, '').strip()
        modBarcode = modColumns[0]
        modProducts.append(BarcodeProduct(modName, modBarcode))
dictStore(modProducts, barcodeProdDict)
######## Food
for foodLine in foodContent.split("\n"):
    foodColumns = foodLine.split(",")
    if len(foodColumns) > 2:
        foodName = foodColumns[0]
        foodBarcode = foodColumns[1]
        foodProducts.append(BarcodeProduct(foodName, foodBarcode))
dictStore(foodProducts, barcodeProdDict)
######## Calories
for calLine in calContent.split("\n"):
    calColumns = calLine.split(",")
    if len(calColumns) > 4:
        calitemName = calColumns[1]
        calSize = calColumns[3]
        calories = calColumns[4]
        caloriesProducts.append(CalProduct(calitemName, calSize, calories))
dictStore(caloriesProducts, calProdDict)

################ Data Sort Formatting
######## Global 
globalOutputString = "Name,Global ID\n"
for k,v in globalProdDict.items():
    globalOutputString += k + ","
    for sv in v:    
        globalOutputString += sv
    globalOutputString += "\n"
globalFormatted = io.StringIO(globalOutputString)
######## Prices
priceOutputString = "Name,Price\n"
for k,v in priceProdDict.items():
    priceOutputString += k + ","
    priceOutputString += v[0]
    priceOutputString = priceOutputString.replace('\"', '')
    priceOutputString += "\n"
priceFormatted = io.StringIO(priceOutputString)
######## Barcodes
barcodeOutputString = "Name,Barcode\n"
for k,v in barcodeProdDict.items():
    barcodeOutputString += k + ","
    for sv in v:    
        barcodeOutputString += sv + "&"  
    barcodeOutputString = barcodeOutputString[:-1]  
    barcodeOutputString += "\n"
barcodeFormatted = io.StringIO(barcodeOutputString)
######## Calories
calOutputString = "Name,Nutritional Data\n"
calOutputString += ("\n".join("{},{}".format(k, v) for k, v in calProdDict.items()))
calOutputString = calOutputString.replace(', ',' ').replace('\') (\'',' Calories - ').replace("\' \'"," ").replace('[(\'','').replace("')]"," Calories")
calFormatted = io.StringIO(calOutputString)

############################ Data into DataFrame ############################
globalDF = pd.read_csv(globalFormatted, sep=',')        # Global
barcodeDF = pd.read_csv(barcodeFormatted, sep=',')      # Barcodes
calDF = pd.read_csv(calFormatted, sep=',')              # Calories
priceDF = pd.read_csv(priceFormatted, sep=',')          # Prices
finalDF = pd.read_csv('final.csv', encoding='UTF-8')    # Final Spreadsheet

################ Combining Data Into A Single Sheet #########################
globalMerge = normMerge(globalDF, finalDF)          # Add Global ID data
barcodeMerge = normMerge(barcodeDF, globalMerge)    # Add Barcode data
calMerge = normMerge(calDF, barcodeMerge)           # Add Calories data
lastMerge = normMerge(priceDF, calMerge)            # Add Price data    

########################## Fixing order of columns ##########################
reorderBarcode = lastMerge.pop('Barcode')
reorderCalorie = lastMerge.pop('Nutritional Data')
reorderPrice = lastMerge.pop('Price')
lastMerge.insert(0, 'Barcode', reorderBarcode)
lastMerge.insert(24, 'Nutritional Data', reorderCalorie)
lastMerge.insert(8, 'Price', reorderPrice)
lastMerge['Price'] = lastMerge['Price'].fillna(0)
lastMerge['Price with markup'] = lastMerge['Price']
lastMerge['Price with commission'] = lastMerge['Price']
lastMerge['Price base'] = lastMerge['Price']
lastMerge.set_index('Global ID', inplace=True)

########################### Create Completed CSV ###########################
lastMerge.to_csv('finalAdded.csv')
print("--- Finished in %s seconds ---" % (time.time() - start_time))