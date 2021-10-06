# importing library
from os import remove
import pandas as pd
import io

#############################################################################################
#                                        # Instructions #                                   #
#    #Match product name                                                                    #
#    #get size of product and calorie                                                       #
#    #input global ID if the starbucks merchant location doesnt have it                     #
#    #GET SKU from sheets bev master sheets                                                 #
#        #editing specifically the barcode cell with SKU with multiple sizes)               #
#    #multiple size SKU joined with &                                                       #
#    #export new CSV                                                                        #
#############################################################################################

class BevProduct:
    itemName = ''
    info = (0)
    
    def __init__(self, itemName, Barcode):
        self.itemName = itemName
        self.info =  (Barcode)

    def __str__(self):
        return self.itemName + ': ' + self.info[0] 

class FoodProduct:
    itemName = ''
    info = (0)
    
    def __init__(self, itemName, Barcode):
        self.itemName = itemName
        self.info =  (Barcode)

    def __str__(self):
        return self.itemName + ': ' + self.info[0] 

class Global:
    itemName = ''
    globalID = ''
    
    def __init__(self, itemName, globalID):
        self.itemName = itemName
        self.globalID =  globalID

    def __str__(self):
        return self.itemName + ': ' + self.globalID

############### Reads Bev CSV
bevReader = open("BevSKU.csv", "r", encoding='UTF-8')
#skip first 6 rows
for i in range(6):
    bevReader.readline()

bevContent = bevReader.read()
bevProducts = [] 

bevOutputString = "Name,Barcode\n"
removeSizes = [" Kids", " Short", " Tall", " Grande", " Venti", " Trenta",
    "Kids ", "Short ", "Tall ", "Grande ", "Venti ", "Trenta "]
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

bevProdDict = {} 
for product in bevProducts:
    if product.itemName in (bevProdDict):
        bevProdDict[product.itemName].append(product.info)
    else:
        bevProdDict[product.itemName] = [product.info]

############### Reads Food CSV
foodReader = open("FoodSKU.csv", "r", encoding='UTF-8')
#skip first 2 rows
for i in range(2):
    foodReader.readline()    

foodContent = foodReader.read()
foodProducts = [] 

foodOutputString = "Name,Barcode\n"
for foodLine in foodContent.split("\n"):
    foodColumns = foodLine.split(",")
    if len(foodColumns) > 2:
        foodName = foodColumns[0]
        foodBarcode = foodColumns[1]
        foodProducts.append(FoodProduct(foodName, foodBarcode))
    else: 
        print(foodColumns)

# food dict
foodProdDict = {} 
for product in foodProducts:
    if product.itemName in (foodProdDict):
        foodProdDict[product.itemName].append(product.info)
    else:
        foodProdDict[product.itemName] = [product.info]

############### Reads Global ID CSV
globalReader = open("master.csv", "r", encoding='UTF-8')
globalReader.readline()    
globalContent = globalReader.read()

globalProducts = [] 

globalOutputString = "Name,Global ID\n"
for globalLine in globalContent.split("\n"):
    globalColumns = globalLine.split(',')
    if len(globalColumns) > 4:
        globalName = globalColumns[2]
        globalID = globalColumns[0]
        globalID = globalID.replace('\"', '')
        globalProducts.append(Global(globalName, globalID))
    else: 
        print(globalColumns)

# global dict
globalProdDict = {} 
for product in globalProducts:
    if product.itemName in (globalProdDict):
        globalProdDict[product.itemName].append(product.globalID)
    else:
        globalProdDict[product.itemName] = [product.globalID]

# Bev CSV formatting
for k,v in bevProdDict.items():
    bevOutputString += k + ", "
    for sv in v:    
        bevOutputString +=  sv + "&"  
    bevOutputString = bevOutputString[:-1]  
    bevOutputString += "\n"

with io.open("bevOutput.csv", "w", encoding="utf-8") as output:
    output.write(bevOutputString)

# Food CSV formatting
for k,v in foodProdDict.items():
    foodOutputString += k + ", "
    for sv in v:    
        foodOutputString +=  sv + "&"  
    foodOutputString = foodOutputString[:-1]  
    foodOutputString += "\n"

with io.open("foodOutput.csv", "w", encoding="utf-8") as output:
    output.write(foodOutputString)

# Global CSV formatting
for k,v in globalProdDict.items():
    globalOutputString += k + ", "
    for sv in v:    
        globalOutputString += sv 
    globalOutputString += "\n"

with io.open("globalOutput.csv", "w", encoding="utf-8") as output:
    output.write(globalOutputString)

### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ###
# convert original CSV to only needed information

# Get Bev into dataframe
bevOutputDF = pd.read_csv('bevOutput.csv', encoding='UTF-8')
# Get Food into dataframe
foodOutputDF = pd.read_csv('foodOutput.csv', encoding='UTF-8')
# Get Starbucks Master Global DF
globalDF = pd.read_csv('globalOutput.csv', encoding='UTF-8')
# Get Final Sheet into dataframe
finalDF = pd.read_csv('final.csv', encoding='UTF-8')

#combine CSV
#completedDF = bevOutputDF.merge(finalDF, on='Name', how='left')
finalDF = finalDF.sort_values(by=['Name','Barcode'])
bevOutputDF = bevOutputDF.sort_values(by=['Name','Barcode'])
foodOutputDF = foodOutputDF.sort_values(by=['Name','Barcode'])
globalDF = globalDF.sort_values(by=['Name'])
finalDF.update(bevOutputDF)
finalDF.update(foodOutputDF)
finalDF.update(globalDF)
finalDF.set_index('Global ID', inplace=True)
finalDF.to_csv('Completed.csv')