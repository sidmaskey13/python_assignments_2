# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age.
import csv

import csv


PEOPLE_LIST = [
    ('Sid','Baneshwor',22),
    ('Ram','Maitidevi',15),
    ('Shyam','Sankhamul',41),
    ('Hari','Teku',12),
]
FILENAME = 'people'


def add_value_csv(people_list, filename):
    with open('p13.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Address", "Age"])
        for i in range(0,len(people_list)):
            writer.writerow(people_list[i])


add_value_csv(PEOPLE_LIST, FILENAME)


