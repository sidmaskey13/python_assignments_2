# Write a function that takes camel-cased strings (i.e.ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

givenString = input('Enter Camel Case String: ')


def snake_case(given_string):
    new_string = ""
    for idx, word in enumerate(given_string):
        if word.isupper():
            if idx != 0:
                new_string += "_"
            new_string += word.lower()
        else:
            new_string += word
    return f"Snake Case: {new_string}"


def kebab_case(given_string):
    new_string = ""
    for idx, word in enumerate(given_string):
        if word.isupper():
            if idx != 0:
                new_string += "-"
            new_string += word.lower()
        else:
            new_string += word
    return f"Kebab Case: {new_string}"


print(snake_case(givenString))
print(kebab_case(givenString))


