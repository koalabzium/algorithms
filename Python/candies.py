
def checkCandy(nodes, candy, index):
    if candy[index] > candy[index+1]:
        return candy[:]
    candy[index] += 1
    if index == 0:
        return candy[:]
    if nodes[index-1] >= nodes[index]:
        candy = checkCandy(nodes, candy, index-1)
    return candy[:]

def candies(nodes):
    candy = [None]*len(nodes)
    candy[0] = 1
    for i in range(1,len(nodes)):
        if nodes[i] > nodes[i-1]: #check if n[i-1] exists!
            candy[i] = 1 + candy[i-1]
        elif nodes[i] == nodes[i-1]:
            candy[i] = candy[i-1]
        else:
            candy[i] = 1
            candy = checkCandy(nodes, candy, i-1)
    return candy


print(candies([1,2,2]))




