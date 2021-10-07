import pandas as pd
import io

################ Class Objects
class BevProduct:
    itemName = ''
    info = (0)
    def __init__(self, itemName, Barcode):
        self.itemName = itemName
        self.info =  (Barcode)
class FoodProduct:
    itemName = ''
    info = (0)
    def __init__(self, itemName, Barcode):
        self.itemName = itemName
        self.info =  (Barcode)
class GlobalProduct:
    itemName = ''
    globalID = ''
    def __init__(self, itemName, globalID):
        self.itemName = itemName
        self.globalID =  globalID
class CalProduct:
    productName = ''
    info = ('', 0)
    def __init__(self, productName, size, calories):
        self.productName = productName
        self.info =  (size, calories)

################ Variables
bevProducts = [] 
bevProdDict = {} 
foodProducts = []
foodProdDict = {}  
globalProducts = []
globalProdDict = {}  
caloriesProducts = [] 
calProdDict = {} 
removeSizes = [" Kids", " Short", " Tall", " Grande", " Venti", " Trenta",
    "Kids ", "Short ", "Tall ", "Grande ", "Venti ", "Trenta "]

################ Reading CSVs
######## Beverages SKU
bevReader = open("BevSKU.csv", "r", encoding='UTF-8')
# skip first six rows
for i in range(6):
    bevReader.readline()
bevContent = bevReader.read()
######## Food SKU
foodReader = open("FoodSKU.csv", "r", encoding='UTF-8')
# skip first two rows
for i in range(2):
    foodReader.readline()    
foodContent = foodReader.read()
######## Reads Global ID 
globalReader = open("Master.csv", "r", encoding='UTF-8')
# skip first row
globalReader.readline()    
globalContent = globalReader.read()
######## Calories Info
calReader = open("Calories.csv", "r", encoding='UTF-8')
# skip first row
calReader.readline()
calContent = calReader.read()

################ Storing Data
######## Beverages
for bevLine in bevContent.split("\n"):
    bevColumns = bevLine.split(",")
    if len(bevColumns) > 4:
        bevName = bevColumns[1]
        for size in removeSizes:
            bevName = bevName.replace(size, '')
        bevBarcode = bevColumns[0]
        bevProducts.append(BevProduct(bevName, bevBarcode))
    else: 
        print(bevColumns)
for product in bevProducts:
    if product.itemName in (bevProdDict):
        bevProdDict[product.itemName].append(product.info)
    else:
        bevProdDict[product.itemName] = [product.info]
######## Food
for foodLine in foodContent.split("\n"):
    foodColumns = foodLine.split(",")
    if len(foodColumns) > 2:
        foodName = foodColumns[0]
        foodBarcode = foodColumns[1]
        foodProducts.append(FoodProduct(foodName, foodBarcode))
    else: 
        print(foodColumns)
for product in foodProducts:
    if product.itemName in (foodProdDict):
        foodProdDict[product.itemName].append(product.info)
    else:
        foodProdDict[product.itemName] = [product.info]
######## Global        
for globalLine in globalContent.split("\n"):
    globalColumns = globalLine.split(',')
    if len(globalColumns) > 4:
        globalName = globalColumns[2]
        globalID = globalColumns[0]
        globalID = globalID.replace('\"', '')
        globalProducts.append(GlobalProduct(globalName, globalID))
    else:
        print(globalColumns)
for product in globalProducts:
    if product.itemName in (globalProdDict):
        globalProdDict[product.itemName].append(product.globalID)
    else:
        globalProdDict[product.itemName] = [product.globalID]
######## Calories
for calLine in calContent.split("\n"):
    calColumns = calLine.split(",")
    if len(calColumns) > 4:
        calitemName = calColumns[1]
        calSize = calColumns[3]
        calories = calColumns[4]
        caloriesProducts.append(CalProduct(calitemName, calSize, calories))
    else: 
        print(calColumns)
for product in caloriesProducts:
    if product.productName in (calProdDict):
        calProdDict[product.productName].append(product.info)
    else:
        calProdDict[product.productName] = [product.info]

################ Data Sort Formatting
######## Beverages
bevOutputString = "Name,Barcode\n"
for k,v in bevProdDict.items():
    bevOutputString += k + ", "
    for sv in v:    
        bevOutputString +=  sv + "&"  
    bevOutputString = bevOutputString[:-1]  
    bevOutputString += "\n"
bevFormatted = io.StringIO(bevOutputString)  
######## Food 
foodOutputString = "Name,Barcode\n"
for k,v in foodProdDict.items():
    foodOutputString += k + ", "
    for sv in v:    
        foodOutputString +=  sv + "&"  
    foodOutputString = foodOutputString[:-1]  
    foodOutputString += "\n"
foodFormatted = io.StringIO(foodOutputString)    
######## Global 
globalOutputString = "Name,Global ID\n"
for k,v in globalProdDict.items():
    globalOutputString += k + ", "
    for sv in v:    
        globalOutputString += sv 
    globalOutputString += "\n"
globalFormatted = io.StringIO(globalOutputString)    
######## Calories
calOutputString = "NName,Nutritional Data\n"
calOutputString += ("\n".join("{},{}".format(k, v) for k, v in calProdDict.items()))
calOutputString = calOutputString.replace(', ',' ')[1:-1].replace("'","").replace("'","").replace("[","").replace("]","").replace("(","").replace(")","")
calFormatted = io.StringIO(calOutputString)

################ Data into DataFrame
######## Beverages
bevDF = pd.read_csv(bevFormatted, sep=',')
######## Food
foodDF = pd.read_csv(foodFormatted, sep=',')
######## Global
globalDF = pd.read_csv(globalFormatted, sep=',')
######## Calories
calDF = pd.read_csv(calFormatted, sep=',')
######## Final Spreadsheet
finalDF = pd.read_csv('final.csv', encoding='UTF-8')

################ Combining Data Into A Single Sheet
######## Beverages
bevMerge = bevDF.merge(finalDF, on='Name', how='right', suffixes=('', '_y'))
bevMerge.drop(bevMerge.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
######## Food
foodMerge = foodDF.merge(bevMerge, on='Name', how='right', suffixes=('', '_y'))
foodMerge.drop(foodMerge.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
######## Global ID
globalMerge = globalDF.merge(foodMerge, on='Name', how='right', suffixes=('', '_y'))
globalMerge.drop(globalMerge.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
######## Calories
calMerge = calDF.merge(globalMerge, on='Name', how='right', suffixes=('', '_y'))
calMerge.drop(calMerge.filter(regex='_y$').columns.tolist(),axis=1, inplace=True)
######## Fixing order of columns
reorderBarcode = calMerge.pop('Barcode')
reorderCalorie = calMerge.pop('Nutritional Data')
calMerge.insert(0, 'Barcode', reorderBarcode)
calMerge.insert(24, 'Nutritional Data', reorderCalorie)
calMerge.set_index('Global ID', inplace=True)
######## Create Completed CSV
calMerge.to_csv('Completed.csv')