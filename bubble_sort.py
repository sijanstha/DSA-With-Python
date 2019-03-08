# Bubble Sort in Python
# Best Case: O(n)
# Worst Case: O(n^2)


def bubble_sort(lists):
    print("Original List:", format(lists))

    # range(0,6) gives from 0 - 5
    for k in range(1, len(lists)):
        flag = 0

        for i in range(0, len(lists) - k):
            if lists[i] > lists[i + 1]:
                temp = lists[i]
                lists[i] = lists[i + 1]
                lists[i + 1] = temp
                flag = 1

        if(flag == 0):
            break

    print("Sorted List: ", format(lists))


if __name__ == '__main__':
    bubble_sort([16, 27, 56, 74, 89, 23, 9])
    bubble_sort([1, 0, 5, 7, 9, 2, 3, 5, 7])
