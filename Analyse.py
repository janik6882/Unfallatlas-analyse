import csv
import os
import json
def extract_loc(path, year, type=0):
    f = open(path, mode="r")
    reader = csv.reader(f, delimiter=";")
    data = list(reader)[1:]
    if type==0:
        loc_data = [[float(i[-2].replace(",", ".")), float(i[-1].replace(",", ".")), year] for i in data]
    elif type==1:
        loc_data = [[float(i[-3].replace(",", ".")), float(i[-2].replace(",", ".")), year] for i in data]
    return loc_data
def out_to_csv(data, filename):
    filename = filename + ".csv"
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(data)
pth1 = os.path.join("Daten", "Unfallorte2016_EPSG25832_CSV", "csv", "Unfallorte_2016_LinRef.csv")
pth2= os.path.join("Daten", "Unfallorte2017_EPSG25832_CSV", "csv", "Unfallorte2017_LinRef.csv")
pth3 = os.path.join("Daten", "Unfallorte2018_EPSG25832_CSV", "csv", "Unfallorte2018_LinRef.csv")
pth4 = os.path.join("Daten", "Unfallorte2019_EPSG25832_CSV", "csv", "Unfallorte2019_LinRef.csv")
data1 =  extract_loc(pth1, 2016)
data2 = extract_loc(pth2, 2017)
data3 = extract_loc(pth3, 2018)
data4 = extract_loc(pth4, 2019, type=1)
data = data1 + data2 + data3 + data4
data.insert(0, ["lng", "lat", "year"])
print data[0:5]
json.dump(data, open("out.json", "w"))
out_to_csv(data4, "out")
