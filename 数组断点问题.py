def binarySearch(lyst):
    left = 0
    right = len(lyst) - 1
    while left <= right:
        middle = (left + right) // 2
        if lyst[middle - 1] > lyst[middle]:
            return middle
        elif lyst[middle] > lyst[-1]:
            left = middle + 1
        else:
            right = middle - 1


a = [4, 6, 1, 2]
print(binarySearch(a))
