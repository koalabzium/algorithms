def longest(a,b):
    mapA = {}
    mapB = {}
    result = []
    while a and b:
        if a[-1] in mapB and mapB[a[-1]]>0:
            result.append(a[-1])
            mapB[a[-1]] -= 1
        elif a[-1] in mapA:
            mapA[a[-1]] += 1
        else:
            mapA[a[-1]] = 1
        if b[-1] in mapA and mapA[b[-1]]>0:
            result.append(b[-1])
            mapA[b[-1]] -= 1
        elif b[-1] in mapB:
            mapB[b[-1]] += 1
        else:
            mapB[b[-1]] = 1
        a.pop()
        b.pop()

    if a:
        while a:
            if a[-1] in mapB and mapB[a[-1]]>0:
                result.append(a[-1])
                mapB[a[-1]] -= 1
            a.pop()
    if b:
        while b:
            if b[-1] in mapA and mapA[b[-1]]>0:
                result.append(b[-1])
                mapA[b[-1]] -= 1
            b.pop()
    return result

print(longest(['A','C','A'],['B','G','C','D','A']))