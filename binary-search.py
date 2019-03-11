
def binary_search(list_of_item, item_to_find):

    list_size = len(list_of_item)

    if list_size == 0:
        return False

    mid_index = list_size // 2

    if list_of_item[mid_index] == item_to_find:
        return True

    else:
        if item_to_find < list_of_item[mid_index]:
            left_list = list_of_item[:mid_index]
            return binary_search(left_list, item_to_find)

        else:
            right_list = list_of_item[mid_index + 1:]
            return binary_search(right_list, item_to_find)


if __name__ == '__main__':
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 0))
