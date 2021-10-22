### Starbucks Adder 
Files needed/Input:
- BevSKU.csv
-- Beverage SKU Getter
- FoodSKU.csv
-- Food SKU Getter
- ModSKU.csv
-- Modifier Item Getter
- Master.csv
-- Global ID Getter
- Calories.csv
-- Calorie Info Getter
- Final.csv
-- Exisiting CSV where needed information is added

File Output:
- finalAdded.csv

Known issues:
Two global ID under one product
- Starbucks Master CSV has duplicate with names being the same. Unsure which one is the correct global ID so grabs it all and concats.
![CSV View](https://i.imgur.com/Hp9og3A.png)
![Completed Excel View](https://i.imgur.com/IsAMhRG.png)

Changelog:
10/21/21
- Changed to completed csv name to finalAdded
  - this was done to know that the new file will be populated right under final
- Stored all data CSV files in a folder 
  - CSVData is where all the data files should be
  - the relative path should only consist of final.csv, SBUXAdd.py, CSVData (Folder), and .vscode (if you are having an error with File Not Found)
- Fixed code clean up and runtime 
  - instead of keeping dupe merge and concat, I made a it go into the one barcode dictionary to prevent duplicates and add new values
  - created functions
- Added modifier barcodes to the adding script