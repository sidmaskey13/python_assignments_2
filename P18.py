# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json
given_data = [
    {"name": "sid", "age": 12},
    {"name": "sam", "age": 22},
    {"name": "suman", "age": 32},
]


def serialize(data):
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)


def deserialize():
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
        print(data)


serialize(given_data)
deserialize()

