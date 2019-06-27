import csv

with open('ONSPD_FEB_2019_UK.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    post_code_abbrv_last = ""
    i = 1
    for row in reader:
        #print(row["pcd"])
        post_code_abbrv = row["pcd"][:-2].replace(" ", "")
        #print(post_code_abbrv)
        if post_code_abbrv != post_code_abbrv_last:
            if row["pcon"] != "":
                csvData = post_code_abbrv + ", " + row["pcon"] + ", " + row["eer"] + ", " + row["rgn"]
                print(i)
                print(csvData)
                with open('ConstitPostCodes_abbrv.csv', 'a') as newFile:
                    fieldnames = ['post_code', 'id_uk_constit', 'id_eu_constit', 'region']
                    writer = csv.DictWriter(newFile, fieldnames=fieldnames)
                    #writer.writeheader() 
                    writer.writerows([{'post_code': post_code_abbrv, 'id_uk_constit': row["pcon"], 'id_eu_constit': row["eer"], 'region': row["rgn"]}])
                print("Row written")
                i = i + 1
                post_code_abbrv_last = post_code_abbrv
