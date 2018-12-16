def fibo_memo(n, memo):
    if n == 1:
        memo[1] = 1
    elif n == 2:
        memo[2] = 1
    else:
        if memo[n]:
            return memo[n]
        else:
            memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]


def fibo_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    memo = [None] * (n + 1)
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fibo(n):
    memo = [None] * (n + 1)
    return fibo_memo(n, memo)


print(fibo(100))
print(fibo_bottom_up(1000))
