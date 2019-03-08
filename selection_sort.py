# selection sort ma min number ko index patta layera swap garinxa
# Best Case: O(n^2)
# Worst Case: O(n^2)

def selection_sort(lists):

    print("unsorted list: ", format(lists))
    for k in range(0, len(lists)):
        min_index = k

        for i in range(k + 1, len(lists)):
            if(lists[i] < lists[min_index]):
                min_index = i

        temp = lists[min_index]
        lists[min_index] = lists[k]
        lists[k] = temp

    print("sorted lists: ", format(lists))


if __name__ == '__main__':
    selection_sort([16, 27, 56, 74, 89, 23, 9, 8])
    # selection_sort([1, 0, 5, 7, 9, 2, 3, 5, 7])
