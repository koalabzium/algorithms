def flattenedIterator(A,B,C):
    iterator = []
    while A or B or C:
        if A:
            iterator.append(A[0])
            A.pop(0)
        if B:
            iterator.append(B[0])
            B.pop(0)
        if C:
            iterator.append(C[0])
            C.pop(0)
    return iterator

print(flattenedIterator([],[4,5],[7,9,10]))