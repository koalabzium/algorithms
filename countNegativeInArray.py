
arr = [[-3,-1,0],[-2,1,2],[-1,3,4]]


def helper(i, j, memo, arr):
    key = str(i) + str(j)
    if key in memo:
        memo[key]
        return memo[key]
    if (i+1<len(arr) and arr[i+1][j] >= 0) and (j+1<len(arr[0]) and arr[i][j+1] >= 0):
        return 1
    elif i+1<len(arr) and arr[i+1][j] >= 0:
        memo[key] = 1 + helper(i,j+1,memo,arr)
        return memo[key]
    elif j+1<len(arr[0]) and arr[i][j+1] >= 0:
        memo[key] = 1 + helper(i+1,j,memo,arr)
        return memo[key]
    elif j+1<len(arr[0]) and i+1<len(arr):
        memo[key] = 1 + helper(i+1,j,memo, arr) + helper(i,j+1,memo, arr)
        return memo[key]
    elif j+1==len(arr[0]) and i+1<len(arr):
        memo[key] = 1 + helper(i+1,j,memo,arr)
        return memo[key]
    elif i+1==len(arr) and j+1<len(arr[0]):
        memo[key] = 1 + helper(i, j + 1, memo, arr)
    else:
        memo[key] = 1
    return memo[key]


def negative(arr):
    memo = {}
    return helper(0,0, memo, arr)

print(negative(arr))