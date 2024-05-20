# Binary search in List

def Binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # This line should be outside the while loop

L = [1, 2, 3, 4, 5, 6, 7]
target = 5
ans = Binary_search(L, target)
print(ans)

