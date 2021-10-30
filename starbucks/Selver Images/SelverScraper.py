import requests # to get image from the web
import shutil # to save it locally

barcodes = []
barcodes_file = open("Barcodes.csv")
for line in barcodes_file:
    barcodes.append(line)

names = []
names_file = open("names.csv")
for line1 in names_file:
    names.append(line1)

## Set up the image URL and filename

# Open the url image, set stream to True, this will return the stream content.
fail_count = 0
success_count = 0
unused_barcodes = []
unused_globalids = []
for i in range(len(barcodes)):

    barcodes[i] = barcodes[i].strip()
    filename = names[i].strip() + ".jpg"
    image_url = "https://www.selver.ee/media/catalog/product/cache/1/image/800x/9df78eab33525d08d6e5fb8d27136e95/" + barcodes[i][0] + "/" + barcodes[i][1] + "/" + barcodes[i] + ".jpg"
    r = requests.get(image_url, stream = True)
    
    if r.status_code == 200:
        r.raw.decode_content = True
            
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        success_count += 1
    else:
        unused_barcodes.append(barcodes[i])
        unused_globalids.append(names[i])
        fail_count += 1
f = open("Unused Barcodes.csv", "w")
f.write(unused_barcodes)
f.close()

f1 = open("Unused Global IDs.csv", "w")
f1.write(unused_globalids)
f1.close()

print("success", success_count)
print('fail', fail_count)
