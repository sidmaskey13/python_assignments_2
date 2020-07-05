# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

givenString = input('Enter string: ')


def check_anagrams(given_string):
    word_length = len(given_string)
    half_word_length = int(word_length/2)
    match = 0
    for i in range(0, half_word_length):
        if given_string[i] == given_string[-i-1]:
            match += 1
    if match == half_word_length:
        return f"{given_string} is Anagram"
    else:
        return f"{given_string} is not Anagram"


print(check_anagrams(givenString))


