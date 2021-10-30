import os

globalid = []
globalid_file = open("globalid.csv")
for line1 in globalid_file:
    globalid.append(line1.strip())

names = []
names_file = open("names.csv")
for line1 in names_file:
    names.append(line1.strip())

for i in range(len(globalid)):
        old_name = r"/Users/Hugo/Box\ Sync/Starship/Selver\ images/" + globalid[i] +".jpg"
        new_name = r"/Users/Hugo/Box\ Sync/Starship/Selver images/" + names[i] +".jpg"
        os.rename(old_name, new_name)
