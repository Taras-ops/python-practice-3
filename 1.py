def remove_duplicates(list):
    arr = []

    for item in list:
        if item not in arr:
            arr.append(item)

    return arr


print(remove_duplicates([[10, 20], [40], [33], [10, 20]]))   # [[10, 20], [40], [33]]
print(remove_duplicates([1, 4, 5, 1, 3, 10, 3]))             # [1, 4, 5, 3, 10]
