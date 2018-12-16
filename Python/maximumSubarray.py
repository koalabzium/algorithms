def max_subarray(array):
    prev_sum = array[0]
    prev_arr = []
    max = []
    max_sum = array[0]
    for i in array:
        if prev_sum + i > i:
            prev_sum = prev_sum + i
            prev_arr.append(i)
        else:
            prev_sum = i
            prev_arr = [i]
        if prev_sum >= max_sum:
            max_sum = prev_sum
            max = prev_arr[:]
    return max

print(max_subarray([-2,2,2,-3,4]))


