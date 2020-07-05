# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

from bisect import bisect_left

NUMBER_LIST = [1, 2, 4, 4, 4, 9, 11, 11]
ITEM = 9


def binary_search(number_list,item):
    i = bisect_left(number_list, item)
    if i != len(number_list) and number_list[i] == item:
        return f"Number {item} found at index {i}"
    return -1


print(binary_search(NUMBER_LIST,ITEM))




