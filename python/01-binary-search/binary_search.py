import math

# O(log n)
def binary_search(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:
        half = (low + high) // 2
        guess = items[half]
        if guess == item:
            return half
        if guess > item:
            high = half - 1
        else:
            low = half + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))


## Exercises:

#1.1 Suppose you have a list with 128 names and are doing a binary search. What would be the maximum number of steps you would take to find the desired name?
print(math.floor(math.log2(128) + 1)) # 8 - assuming there will be 8 comparisons in the code

#1.2 Suppose you double the size of the list. What would be the maximum number of steps now?
len_list = 128
double_len_list = 128 * 2
print(math.floor(math.log2(double_len_list) + 1)) # 9 - assuming there will be 8 comparisons in the code
