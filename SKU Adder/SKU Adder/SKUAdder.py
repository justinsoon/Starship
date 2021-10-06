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
    
    def __init__(self, itemName, itemSKU):
        self.itemName = itemName
        # if product is already in the set modify it size and calories
        self.info =  (itemSKU)

    def __str__(self):
        return self.itemName + ': ' + self.info[0] 

############### Reads CSV
fileReader = open("BevSKU.csv", "r", encoding='UTF-8')
for i in range(6):
    fileReader.readline()

fileContent = fileReader.read()

products = [] 

z_output = "Name,ItemSKU\n"
removeSizes = ["Venti", "Tall", "Short", "Grande", "Kids", "Trenta"]
for line in fileContent.split("\n"):
    columns = line.split(",")
    if len(columns) > 4:

        name = columns[1]
        for size in removeSizes:
            name = name.replace(size, '')
        itemSKU = columns[0]
        #z_output += name  + "," + itemSKU +"\n"
        #print(z_output)
        products.append(Product(name, itemSKU))
    else: 
        print(columns)

prodDict = {} 
for product in products:
    if product.itemName in (prodDict):
        prodDict[product.itemName].append(product.info)
    else:
        prodDict[product.itemName] = [product.info]


for k,v in prodDict.items():
    z_output += k
    for sv in v:    
        z_output +=  "," 
    z_output += "\n"

print(z_output)


with io.open("output.txt", "w", encoding="utf-8") as output:
    outputString = ("\n".join("{},{}".format(k, v) for k, v in prodDict.items()))
    outputString = outputString.replace('\', \'','&').replace('\']', '').replace('[\'','')
    output.write(outputString)

    #Teavana® Iced Peach Green Tea Lemonade : ['011105756&011105757&011105758&011126350&011126351&011126352']
    #Teavana® Iced Peach Green Tea Lemonade,011105756&011105757&011105758&011126350&011126351&011126352
#df = pd.DataFrame.from_dict(prodDict)
#df.to_csv (r'output.csv', index = False, header=True)

# Get Bev into dataframe
bevDF = pd.read_csv('BevSKU.csv', encoding='UTF-8')
# Get Final Sheet into dataframe
finalDF = pd.read_csv('final.csv', encoding='UTF-8')
# Get Starbucks Master Global DF
globalDF = pd.read_csv('master.csv', encoding='UTF-8')

#df = pd.merge(finalDF,bevDF, on='Barcode', how="left")
#pd.merge(finalDF, globalDF, on=['Global ID',  'Name'], how='left')

#finalDF.to_csv('output.csv', index=False)