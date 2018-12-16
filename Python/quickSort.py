def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr) // 2
    swap(arr, pivot, -1)
    left = 0
    right = len(arr) - 2
    first_left = None
    first_right = None
    while left <= right:
        if arr[right] <= arr[-1]:
            first_right = right
        elif arr[right] > arr[-1]:
            right -= 1
        if arr[left] >= arr[-1]:
            first_left = left
        elif arr[left] < arr[-1]:
            left += 1

        if first_left is not None and first_right is not None:
            swap(arr, first_left, first_right)
            first_left = None
            first_right = None
            left+=1
            right-=1
    swap(arr, left, -1)
    arr[:left] = quickSort(arr[:left])
    arr[left+1:] = quickSort(arr[left+1:])
    return arr


print(quickSort(arr))
