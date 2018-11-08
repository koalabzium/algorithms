import math


def sqrt_bad(n):
    smaller = 0
    larger = 0
    for i in range(n):
        if i ** 2 >= n:
            smaller = i - 1
            larger = i
            break
    if abs(n - (smaller ** 2)) < abs(n - (larger ** 2)):
        return smaller
    return larger


def mysqrt(n):
    if n == 1:
        return 1
    else:
        return sqrt(1, n - 1, n)


def sqrt(b, e, n):
    pivot = (e + b) // 2
    if pivot ** 2 == n:
        return pivot
    elif pivot ** 2 < n and (pivot + 1) ** 2 > n:
        return pivot
    if pivot ** 2 < n:
        return sqrt(pivot + 1, e, n)
    elif pivot ** 2 > n:
        return sqrt(b, pivot - 1, n)


print(mysqrt(1))
