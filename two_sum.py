# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def find(list, target):
    sum = 0
    for x in range(len(list)):
        diff = target - list[x]

        if diff in list:
            return [x, list.index(diff)]

    return "not"


if __name__ == '__main__':
    print(find([2, 7, 11, 15], 9))

# TODO Implement in JAVA
