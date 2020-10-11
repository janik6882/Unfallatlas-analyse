import csv
import os
import json
def extract_loc(path):
    f = open(path, mode="r")
    reader = csv.reader(f, delimiter=";")
    data = list(reader)[1:]
    loc_data = [[float(i[-2].replace(",", ".")), float(i[-1].replace(",", "."))] for i in data]
    return loc_data

pth1 = os.path.join("Daten", "Unfallorte2016_EPSG25832_CSV", "csv", "Unfallorte_2016_LinRef.csv")
pth2= os.path.join("Daten", "Unfallorte2017_EPSG25832_CSV", "csv", "Unfallorte2017_LinRef.csv")
pth3 = os.path.join("Daten", "Unfallorte2018_EPSG25832_CSV", "csv", "Unfallorte2018_LinRef.csv")
pth4 = os.path.join("Daten", "Unfallorte2019_EPSG25832_CSV", "csv", "Unfallorte2019_LinRef.csv")
data1 =  extract_loc(pth1)
data2 = extract_loc(pth2)
data3 = extract_loc(pth3)
data4 = extract_loc(pth4)
data = data1 + data2 + data3 + data4
data.insert(0, ["lng", "lat"])
print data[0:5]
json.dump(data, open("out.json", "w"))
