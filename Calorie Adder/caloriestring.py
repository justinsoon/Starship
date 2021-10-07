# importing library
import pandas as pd
import io

#############################################################################################
#                                        # Instructions #                                   #
#    #read product name                                                                     #
#    #get size of product and calorie                                                       #
#    #Caramel Apple Spice: Kids - 220, Short - 220, Tall - 310, Grande - 380, Venti - 460   #
#    #match name with other CSV                                                             #
#        #finalCSV = pd.read_csv("Final.csv", encoding='latin1')                            #
#    #find Name column                                                                      #
#        #find nutrional data column in row                                                 #
#            #append nutrional data with edited string                                      #
#    #export new CSV                                                                        #
#############################################################################################

class Product:
    productName = ''
    info = ('', 0)
    
    def __init__(self, productName, size, calories):
        self.productName = productName
        # if product is already in the set modify it size and calories
        self.info =  (size, calories)

    def __str__(self):
        return self.productName + ': ' + self.info[0] + ' - ' + self.info[1] + ' Calories'

#############################################################################################
###################################### Dataframe method #####################################
#############################################################################################

# Get Calories CSV
#caloriesCSV = pd.read_csv('Calories.csv', encoding='UTF-8')

# Removing duplicated product name, keeps first value
# groups by product name and calories under the product name
#df = caloriesCSV[caloriesCSV.duplicated('Product Name', keep="first")].groupby('Product Name')['Calories'].apply(list).reset_index()

############### Creating file
#df.to_csv('CaloriesInfo.csv', index=False)

############## Appending file
# read the final csv
#finalCSV = pd.read_csv('Final.csv', encoding='latin1')
# get all the column of final CSV
#finalCsvColumns = pd.DataFrame(columns=finalCSV.columns)
# get all the column of Calories CSV
#CaloriesColumns = pd.DataFrame(columns=caloriesCSV.columns)
# opening final csv and appending it
#with open('final.csv', 'a') as f:  
    # go through all rows of final.csv
#    for j, row in finalCSV.iterrows():
        # go through all rows of calories csv
#        for k, row in caloriesCSV.itemrows():
            # Go through the "Name" column from final.CSV and match it with the "Product Name" column from CaloriesCSV
#            if pd.isna(row["Name"]) is pd.isna(row["Product Name"]):
#                # find nutrional column out of all the columns in final csv 
#                for nutrionalColumn in finalCsvColumns:
#                    # save DF to csv
#                    df.to_csv(f, header=False)

#with io.open("output.txt", "w", encoding="utf-8") as output:
    #output.write(df.to_string())

#############################################################################################
###################################### Text Replace Method ##################################
#############################################################################################

############### Reads CSV
fileReader = open("Calories.csv", "r", encoding='UTF-8')
fileReader.readline()
  
fileContent = fileReader.read()

products = [] 
for line in fileContent.split("\n"):
    columns = line.split(",")
    if len(columns) > 4:
        itemName = columns[1]
        size = columns[3]
        calories = columns[4]
        products.append(Product(itemName, size, calories))
    else: 
        print(columns)

prodDict = {} 
for product in products:
    if product.productName in (prodDict):
        prodDict[product.productName].append(product.info)
    else:
        prodDict[product.productName] = [product.info]
  
############### Creating file
with io.open("output.txt", "w", encoding="utf-8") as output:
    outputString = ("\n".join("{}:\t{}".format(k, v) for k, v in prodDict.items()))
    outputString = outputString.replace(', ',' ')[1:-1].replace("'","").replace("'","")
    print(outputString)

#df = pd.DataFrame.from_dict(prodDict, orient='index')
#df = df.transpose()
#df.to_csv (r'output.csv', index = False, header=True)
    
#############################################################################################
############################################# DEBUGGING #####################################
#############################################################################################

#print(text)
#print(df.to_string())
