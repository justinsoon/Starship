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
#        #append nutrional data with edited string                                          #
#    #export new CSV                                                                        #
#############################################################################################

class Product:
    itemName = ''
    info = (0)
    
    def __init__(self, itemName, Barcode):
        self.itemName = itemName
        # if product is already in the set modify it size and calories
        self.info =  (Barcode)

    def __str__(self):
        return self.itemName + ': ' + self.info[0] 

############### Reads CSV
fileReader = open("BevSKU.csv", "r", encoding='UTF-8')
#skip first 6 rows
for i in range(6):
    fileReader.readline()

fileContent = fileReader.read()

products = [] 

outputString = "Name,Barcode\n"
removeSizes = [" Kids", " Short", " Tall", " Grande", " Venti", " Trenta",
    "Kids ", "Short ", "Tall ", "Grande ", "Venti ", "Trenta "]
for line in fileContent.split("\n"):
    columns = line.split(",")
    if len(columns) > 4:

        name = columns[1]
        for size in removeSizes:
            name = name.replace(size, '')
        Barcode = columns[0]
        products.append(Product(name, Barcode))
    else: 
        print(columns)

prodDict = {} 
for product in products:
    if product.itemName in (prodDict):
        prodDict[product.itemName].append(product.info)
    else:
        prodDict[product.itemName] = [product.info]


for k,v in prodDict.items():
    outputString += k + ", "
    for sv in v:    
        outputString +=  sv + "&"  
    outputString = outputString[:-1]  
    outputString += "\n"

with io.open("output.csv", "w", encoding="utf-8") as output:
    output.write(outputString)

### ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ###
# convert original CSV to only needed information

# Get Bev into dataframe
outputDF = pd.read_csv('output.csv', encoding='UTF-8')
# Get Final Sheet into dataframe
finalDF = pd.read_csv('final.csv', encoding='UTF-8')
# Get Starbucks Master Global DF
globalDF = pd.read_csv('master.csv', encoding='UTF-8')


#combine CSV
completedDF = pd.concat([finalDF, outputDF[~outputDF.Name.isin(finalDF.Name)]])
completedDF.update(finalDF)
completedDF.set_index('Global ID', inplace=True)
completedDF.to_csv('completed.csv')

