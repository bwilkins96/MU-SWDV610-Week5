# SWDV 610: Data Structures and Algorithms
# Functions that return whether 2 strings are anagrams

def is_anagram(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort()
    s2_list.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if s1_list[pos] != s2_list[pos]:
            matches = False

        pos += 1

    return matches

def is_anagram_2(s1, s2):
    if len(s1) != len(s2): return False
    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort()
    s2_list.sort()

    for i in range(len(s1_list)):
        if s1_list[i] != s2_list[i]:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram('abcde', 'edcba'))
    print(is_anagram('asdas', 'ysdawwqw'))
    print()
    print(is_anagram_2('abcde', 'edcba'))
    print(is_anagram_2('asdas', 'ysdawwqw'))
