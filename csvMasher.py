import csv

with open('ONSPD_FEB_2019_UK_AB.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["pcd"] + ", " + row["pcon"] + ", " + row["eer"] + ", " + row["rgn"])
