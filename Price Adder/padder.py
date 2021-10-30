import pandas as pd
from thefuzz import process
import io
import time
start_time = time.time()
######## Merge two DFs
def normMerge(firstDF, lastDF, data):
    # Searching for string match
    print (data + ' - Searching matches...')
    firstDF['tempName_2'] = firstDF['Name'].apply(lambda x: process.extractOne(x, lastDF['Name'].to_list(),score_cutoff=95)) #cutoff value is percentage of match needed
    tempName_list = firstDF['tempName_2'].to_list()
    tempName_list = [_[0] if _ != None else None for _ in tempName_list]
    firstDF['tempName_2'] = tempName_list
    # Merging data
    firstDF = firstDF.merge(lastDF, left_on = 'tempName_2', right_on = 'Name', how='left', suffixes=('','_2'))
    firstDF[data] = firstDF[data+ '_2']
    firstDF.drop(firstDF.filter(regex='_2$').columns.tolist(),axis=1, inplace=True)
    print (data + ' - Added!')    
    return firstDF

############################ Data into DataFrame ############################
currentDF = pd.read_csv('current.csv', encoding='UTF-8') 
priceDF = pd.read_csv('final.csv', usecols = ['Name','Price']) #Price
################ Combining Data Into A Single Sheet #########################
merge = normMerge(currentDF, priceDF, 'Price')        # Add Global ID data

########################## Fixing order of columns ##########################
reorderPrice = merge.pop('Price')
merge.insert(8, 'Price', reorderPrice)
merge['Price'] = merge['Price'].fillna(0)           
merge['Price with markup'] = merge['Price']
merge['Price with commission'] = merge['Price']
merge['Price base'] = merge['Price']
merge.set_index('Global ID', inplace=True)

########################### Create Completed CSV ###########################
merge.to_csv('finalAdded.csv')
print("--- Finished in %s seconds ---" % (time.time() - start_time))
