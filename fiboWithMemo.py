
def fibo(n, memo):
    print(n)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        if memo[n]:
            return memo[n]
        else:
            memo[n] = fibo(n-1, memo)+fibo(n-2, memo)
        return memo[n]

m = []
print(fibo(6,m))