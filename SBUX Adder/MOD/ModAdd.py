import pandas as pd
import io

class ModProduct:
    itemName = ''
    info = ''
    def __init__(self, itemName, barCode):
        self.itemName = itemName
        self.info =  (barCode)

modProducts = [] 
modProdDict = {} 
removeSizes = ["Kids", "Short", "Tall", "Grande", "Venti", "Trenta"]
removeType = ['Add', 'Extra', 'Light', 'Substitute','Sub', 'No ', ' add', ' extra', ' light', ' sub', ' regular', ' no', 
    ' Modifier', ' Single', ' Double', ' Triple', 'Quad', 'Solo ', 'Doppio ', 'Triple ', ' modifier', ' modifier extra',
    ' modifier light', ' modifier no', ' modifier regular', ' modifier sub', 'Extra ', 'Light ', 'Add ']

######## Modifier SKU
modReader = open("ModSKU.csv", "r", encoding='UTF-8')
# skip first six rows
for i in range(6):
    modReader.readline()
modContent = modReader.read()

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
        modProducts.append(ModProduct(modName, modBarcode))
for product in modProducts:
    if product.itemName in (modProdDict):
        modProdDict[product.itemName].append(product.info)
    else:
        modProdDict[product.itemName] = [product.info]


######## Modifiers
modOutputString = "Name,Barcode\n"
for k,v in modProdDict.items():
    modOutputString += k + ","
    for sv in v:    
        modOutputString += sv + "&"  
    modOutputString = modOutputString[:-1]  
    modOutputString += "\n"
with io.open("output.txt", "w", encoding="utf-8") as output:
    output.write(modOutputString)
    #print (modOutputString)
    print (modProdDict)
