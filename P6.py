# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

givenString = input('Enter string: ')
name_list = [
    'sid', 'ram', 'hazard', 'shyam', 'martial', 'pulisic', 'mount', 'willian', 'terry', 'john', 'tomori'
]


def check_name_list(given_string):
    found_name = 0
    given_string = given_string.lower()
    for i in name_list:
        if given_string == i:
            found_name = 1

    if found_name == 1:
        return f"{given_string} is found in the list"
    else:
        return f"{given_string} is not found in the list"


print(check_name_list(givenString))


