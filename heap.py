# [r,d1,d2,d11,d12,d21,d22] 2*index, 2*index+1
# 4 ceil(index-2)/2 - rodzic index*2+1 index*+2
import math

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


def checkHeap(heap):
    if 1 < len(heap):
        left = heap[1]
    else:
        return heap
    if 2 < len(heap):
        right = heap[2]
    else:
        if heap[0] > left:
            swap(heap,0,1)
        return heap
    if heap[0] > left or heap[0] > right:
        if right >= left:
            swap(heap, 0, 1)
        else:
            swap(heap, 0, 2)
    return heap


def heapInsert(heap, node):
    heap.append(node)
    if node < heap[0]:
        swap(heap, 0, -1)
    checkHeap(heap)

heapInsert(heap,4)
heapInsert(heap,5)
heapInsert(heap,2)



print(heap)