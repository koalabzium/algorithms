def merge(a,b):
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    c += a
    c += b
    return c

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    half = len(arr)//2
    return merge(mergeSort(arr[:half]),mergeSort(arr[half:]))


print(mergeSort([2,4,34,2,5,3,2,5,6,7,9,6,4]))