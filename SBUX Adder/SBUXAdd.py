import pandas as pd
from thefuzz import process
import io
import time
start_time = time.time()
################ Class Objects
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
def normMerge(firstDF, lastDF, data):
    print (data + ' - Searching matches...')
    firstDF['tempName_2'] = firstDF['Name'].apply(lambda x: process.extractOne(x, lastDF['Name'].to_list(),score_cutoff=95)) #cutoff value is percentage of match
    tempName_list = firstDF['tempName_2'].to_list()
    tempName_list = [_[0] if _ != None else None for _ in tempName_list]
    firstDF['tempName_2'] = tempName_list
    print (tempName_list)

    firstDF = firstDF.merge(lastDF, left_on = 'tempName_2', right_on = 'Name', how='left', suffixes=('','_2'))
    firstDF[data] = firstDF[data+ '_2']
    firstDF.drop(firstDF.filter(regex='_2$').columns.tolist(),axis=1, inplace=True)
    print (data + ' - Added!')    
    return firstDF

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
bevContent = readCSV('CSVData/BevSKU.csv', 6)       # Beverages SKU - skip first six row
modContent = readCSV('CSVData/ModSKU.csv', 6)       # Modifier SKU - skip first six row
foodContent = readCSV('CSVData/FoodSKU.csv', 2)     # Food SKU- skip first two row
calContent = readCSV('CSVData/Calories.csv', 1)     # Calories Info - skip first row

################ Storing Data
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
globalDF = pd.read_csv('CSVData/master.csv', usecols = ['Name','Global ID']) #Global
priceDF = pd.read_csv('CSVData/master.csv', usecols = ['Name','Price']) #Price
barcodeDF = pd.read_csv(barcodeFormatted, sep=',')      # Barcodes
calDF = pd.read_csv(calFormatted, sep=',')              # Calories
finalDF = pd.read_csv('final.csv', encoding='UTF-8')    # Final Spreadsheet

################ Combining Data Into A Single Sheet #########################
globalMerge = normMerge(finalDF, globalDF, 'Global ID')        # Add Global ID data
lastMerge = normMerge(globalMerge, priceDF, 'Price')           # Add Global ID data
barcodeMerge = normMerge(barcodeDF, globalMerge, 'Barcode')    # Add Barcode data
calMerge = normMerge(calDF, barcodeMerge, 'Nutritional Data')  # Add Calories data

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
