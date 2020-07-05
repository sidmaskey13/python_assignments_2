# Write an if statement to determine whether a variable holding a year
# is a leap year.

while True:
    try:
        GIVEN_NUMBER = int(input('Enter Number: '))
    except ValueError:
        print("Not valid integer. TRY AGAIN!!")
        continue
    else:
        break


def leap_year(given_number):
    if given_number % 4 == 0:
        return f"{given_number} is leap year"
    return f"{given_number} is not leap year"


print(leap_year(GIVEN_NUMBER))







