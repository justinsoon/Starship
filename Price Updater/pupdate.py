import pandas as pd, numpy as np
from thefuzz import process
import time
start_time = time.time()

######## getting the true price column
def cleanVal(df):
    df['Price'] = df.Price.mask(df.Price.str.len() == 8, df.Price.str[4:])
    df['Price'] = df.Price.mask(df.Price.str.len() == 7, df.Price.str[3:])
    df['Price'] = df.Price.mask(df.Price.str.len() == 6, df.Price.str[3:])
    return df

######## Fixing order of columns
def cleanDF(df):
    reorderPrice = df.pop('Price')
    df.insert(8, 'Price', reorderPrice)
    df['Price'] = df['Price'].fillna(0)           
    df['Price with markup'] = df['Price']
    df['Price with commission'] = df['Price']
    df['Price base'] = df['Price']
    df.set_index('Global ID', inplace=True)
    return df

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
    firstDF = firstDF.replace(np.nan, '')
    firstDF["Price"] = [''.join(i) for i in zip(firstDF["Price"].map(str),firstDF["Price_2"].map(str))]
    cleanVal(firstDF)
    firstDF.drop(firstDF.filter(regex='_2$').columns.tolist(),axis=1, inplace=True)
    print (data + ' - Added!')    
    return firstDF

############################ Data into DataFrame ############################
currentDF = pd.read_csv('current.csv', encoding='UTF-8') 
priceDF = pd.read_csv('final.csv', usecols = ['Name','Price']) #Price
################ Combining Data Into A Single Sheet #########################
merge = normMerge(currentDF, priceDF, 'Price')        # Add Global ID data
cleanDF(merge)
########################### Create Completed CSV ###########################
merge.to_csv('finalAdded.csv')
print("--- Finished in %s seconds ---" % (time.time() - start_time))