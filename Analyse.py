import csv
import os
import json
def extract_loc(path):
    f = open(path, mode="r")
    reader = csv.reader(f, delimiter=";")
    data = list(reader)[1:]
    loc_data = [[i[-2], i[-1]] for i in data]
    return loc_data

pth = os.path.join("Daten", "Unfallorte2016_EPSG25832_CSV", "csv", "Unfallorte_2016_LinRef.csv")
data =  extract_loc(pth)
data.insert(0, ["lng", "lat"])
print data[0:5]
json.dump(data, open("out.json", "w"))
