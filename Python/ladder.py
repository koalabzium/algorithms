def helper(n, ways, step):
    print(ways, step)
    res1 = 0
    res2 = 0
    if step == n:
        return 1
    if step < n-1:
        res1 += helper(n, ways, step+1)
        res2 += helper(n, ways, step+2)
    elif step < n:
        res1 += helper(n, ways, step+1)
    ways = res1 + res2
    return ways


def ladder(n):
    step = 0
    ways = 0
    ways += helper(n, step, ways)
    return ways

print(ladder(3))