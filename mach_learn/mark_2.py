import csv

results = []
with open("/home/hanif/pymach/data/melb_data.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

print(results.head(5))
