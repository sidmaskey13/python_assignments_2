# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.
while True:
    try:
        GIVEN_NUMBER = int(input('Enter number: '))
    except ValueError:
        print("Not valid integer. TRY AGAIN!!")
        continue
    else:
        break


def is_prime(given_number):
    prime = 0
    for i in range(1,given_number):
        if given_number % i == 0:
            prime +=1

    if prime < 2:
        return f"{given_number} is Prime Number"
    else:
        return f"{given_number} is not Prime Number"


print(is_prime(GIVEN_NUMBER))


