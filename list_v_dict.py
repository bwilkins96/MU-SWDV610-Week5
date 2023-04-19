# SWDV 610: Data Structures and Algorithms
# Code that utilizes the list and dictionary data types

from time import time

def main():
    test_list = [1, 2, 3, 4]
    test_list.append(5)
    test_list.append(6)

    print('list''\n------------------------')
    print(test_list)           # -> [1, 2, 3, 4, 5, 6]
    test_list.pop()
    print(test_list)           # -> [1, 2, 3, 4, 5]
    test_list.pop(2)
    print(test_list)           # -> [1, 2, 4, 5]
    test_list[0] = 55
    print(test_list)           # -> [55, 2, 4, 5]

    test_dict = {'a': 1, 'b': 2}
    test_dict['c'] = 3

    print('\ndictionary\n------------------------')
    print(test_dict)           # ->  {'a': 1, 'b': 2, 'c': 3}
    test_dict['a'] = 42
    print(test_dict)           # ->  {'a': 42, 'b': 2, 'c': 3}
    del test_dict['b']
    print(test_dict)           # ->  {'a': 1, 'c': 3}


    # Test the difference in time between adding 100 items to
    # a dictionary vs adding 100 items to the front of a list
    input()
    print('Insertion time test\n------------------------')
    for i in range(10):
        test_list = []
        test_dict = {}

        t1 = time()
        for i in range(25000):
            test_list.insert(0, i)
        t2 = time()

        t3 = time()
        for i in range(25000):
            test_dict[i] = i
        t4 = time()

        print('\nList insertion:', (t2-t1)*1000, 'ms')
        print('Dictionary insertion', (t4-t3)*1000, 'ms')

if __name__ == '__main__': main()
