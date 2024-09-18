def is_sorted_list(list):
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            return False

    return True


print(is_sorted_list([1, 2, 4, 7, 8, 10]))   # True
print(is_sorted_list([4, 1, 3, 7, 8, 2]))    # False
