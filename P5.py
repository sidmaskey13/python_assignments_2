# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

people =[]
my_tuple = ('siddhartha','maskey',22)
f1_tuple = ('gopal','joshi',12)
f2_tuple = ('ram','shrestha',25)
f3_tuple = ('hari','rai',20)


def add_tuple_list():
    people.append(my_tuple)
    people.append(f1_tuple)
    people.append(f2_tuple)
    people.append(f3_tuple)


def sort_fname(people_list):
    sorted_list = sorted(people_list, key=lambda x: x[0])
    return f"Sorted by first name:{sorted_list}"


def sort_lname(people_list):
    sorted_list = sorted(people_list, key=lambda x: x[1])
    return f"Sorted by last name:{sorted_list}"


def sort_age(people_list):
    sorted_list = sorted(people_list, key=lambda x: x[2])
    return f"Sorted by age:{sorted_list}"


add_tuple_list()
print(sort_age(people))
print(sort_fname(people))
print(sort_lname(people))


