# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

name_list = []


def add_name_list(given_string):
    name_list.append(given_string)


def display_name_list():
    name_list.sort()
    return f"Name list is {name_list}"


print('Enter 5 names')
for i in range(0,5):
    GIVEN_NAME = input(f"{i+1}. Enter a name: ")
    add_name_list(GIVEN_NAME)


print(display_name_list())


