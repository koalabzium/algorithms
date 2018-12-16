def palindrome(n):
    n = str(n)
    i = 0
    j = len(n) - 1
    while i<j:
        if n[i] != n[j]:
            return False
        i += 1
        j -= 1
    return True

