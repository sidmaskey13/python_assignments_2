# Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.

GIVEN_LIST = [-25, -10, -7, -3, 2, 4, 8, 10]

def find_sum_zero(list):
    n = len(list)
    found = True
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (list[i] + list[j] + list[k] == 0):
                    print(list[i], list[j], list[k])
                    found = True
    if (found == False):
        print("List value doesnt equal 0")




find_sum_zero(GIVEN_LIST)



