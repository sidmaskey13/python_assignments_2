# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

GIVEN_STRING = input('Enter string: ')


def check_parenthese(given_string):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    temp = []
    for i in given_string:
        if i in open_list:
            temp.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(temp) > 0) and
                    (open_list[pos] == temp[len(temp) - 1])):
                temp.pop()
            else:
                return f"{given_string} is Invalid"
    if len(temp) == 0:
        return f"{given_string} is Valid"
    return f"{given_string} is Invalid"


print(check_parenthese(GIVEN_STRING))



