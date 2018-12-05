def anagrams(a,b):
    letters = {}
    for l in a:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    for l in b:
        if l in letters:
            if letters[l] == 1:
                letters.pop(l)
            else:
                letters[l] -= 1
        else:
            return False
    if letters == {}:
        return True
    return False

print(anagrams('zosidga','aizosd'))