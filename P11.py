# Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?

GIVEN_FILENAME = input('Enter filename: ')


def extract_extension(given_filename):
    filename = given_filename.split(".", 1)[0]
    extension = given_filename.split(".", 1)[1]
    return f"Extension is {extension} and filename is {filename}"


print(extract_extension(GIVEN_FILENAME))


