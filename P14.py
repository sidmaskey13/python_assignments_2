# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.

import csv
with open('p13.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

