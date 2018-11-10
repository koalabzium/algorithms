import math

#MINIMUM HEAP


heap = []


def swap(list, a, b):
    tmp = list[a]
    list[a] = list[b]
    list[b] = tmp


def getParent(index):
    return math.ceil((index - 2) / 2)


def getLeft(index):
    return index * 2 + 1


def getRight(index):
    return index * 2 + 2

def bubbleUp(heap, index):
    prev = getParent(index)
    if prev >= 0 and heap[prev] > heap[index]:
        swap(heap, index, prev)
        return bubbleUp(heap, prev)
    return heap[:]


def bubbleDown(heap,index):
    #TODO
    l = len(heap) - 1
    

def insert(heap, n):
    heap.append(n)
    return bubbleUp(heap,len(heap)-1)

def getMin(heap):
    min = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heap = bubbleDown(heap,0)
    print(heap)
    return min


print(insert(heap,2))
print(insert(heap,7))
print(insert(heap,9))
print(insert(heap,1))
print(insert(heap,3))
print(insert(heap,17))
print(insert(heap,5))
print(insert(heap,0))