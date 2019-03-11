# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true

# Example 2:

# Input: [1,2,3,4]
# Output: false

# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true


def contains_dup(list):
    num_to_compare = list[0]
    for x in range(1, len(list)):
        print(list[x])
        if list[x] == num_to_compare:
            print("true")
        else:
            num_to_compare = list[x]


if __name__ == '__main__':
    contains_dup([1, 2, 3, 4, 1])
