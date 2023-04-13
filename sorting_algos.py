# SWDV 610: Data Structures and Algorithms
# Sorting functions implementing bubble sort, selection sort, and insertion sort

def bubble_sort(lst):
    """Sorts a list in-place using the bubble sort algorithm"""
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False
    
    return lst

def selection_sort(lst):
    """Sorts a list in-place using the selection sort algorithm"""
    for fill_idx in range(len(lst)-1, 0, -1):

        max_idx = 0
        for i in range(1, fill_idx+1):
            if lst[i] > lst[max_idx]:
                max_idx = i

        lst[max_idx], lst[fill_idx] = lst[fill_idx], lst[max_idx]

    return lst

def insertion_sort(lst):
    """Sorts a list in-place using the insertion sort algorithm"""
    for i in range(1, len(lst)):
        val = lst[i]
        position = i
        
        while position > 0 and lst[position-1] > val:
            lst[position] = lst[position-1]
            position -= 1

        lst[position] = val

    return lst

if __name__ == '__main__':
    test = [5, 6, 8, 1, 3, 9, 2, 4, 7, 10]
    
    print(bubble_sort(test[:]))
    print()
    print(selection_sort(test[:]))
    print()
    print(insertion_sort(test[:]))