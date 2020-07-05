# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.
from functools import reduce

people_list = [
    ('gopal', 'joshi', 12), ('hari', 'rai', 20),
    ('siddhartha', 'maskey', 22), ('ram', 'shrestha', 16),
    ('suraj', 'khatri', 19),('kumar','hona','')
               ]

def calculate_average_age(given_list):
    age_sum = 0
    total_names = len(given_list)

    for fname, lname, age in given_list:
        if age != "":
            age_sum += int(age)
    avg = age_sum/total_names
    print(f"Average age is {avg}")

    for fname, lname, age in given_list:
        if age != "":
            if avg > int(age):
                print(f"{fname} {lname}, {age} is younger than average")
            elif avg < int(age):
                print(f"{fname} {lname}, {age} is older than average")
        else:
            print(f"{fname} {lname} age is not given")
    return


print(calculate_average_age(people_list))


