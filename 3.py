def is_list_palindrome(list):
    palindromed_list = list[::-1]

    for i in range(0, len(list)):
        if palindromed_list[i] != list[i]:
            return False

    return True


print(is_list_palindrome([1, 5, 6, 5, 1]))   # True
print(is_list_palindrome([1, 2, 3, 2, 2]))   # False
print(is_list_palindrome([1, 1]))            # True
