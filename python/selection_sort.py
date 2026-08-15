# O(n)
def find_smallest_index(items):
    smallest = items[0]
    smallest_index = 0
    for index in range(1, len(items)):
        if items[index] < smallest:
            smallest = items[index]
            smallest_index = index
    return smallest_index

# O(n^2)
def selection_sort(items):
    sorted_items = []
    for _ in range(len(items)):
        smallest_index = find_smallest_index(items)
        sorted_items.append(items.pop(smallest_index))
    return sorted_items


print(selection_sort([8, 9, 7, 5, 6, 5, 2, 3, 4, 5, 3, 9, 2, 4, 6, 5, 3, 2, 4, 0, 8]))
