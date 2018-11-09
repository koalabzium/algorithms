
def fibo(n, memo):
    if n == 1:
        memo[1] = 1
    elif n == 2:
        memo[2] = 1
    else:
        if memo[n]:
            return memo[n]
        else:
            memo[n] = fibo(n-1, memo)+fibo(n-2, memo)
    return memo[n]

n=6
memo = [None for _ in range(n+1)]
print(fibo(n,memo))