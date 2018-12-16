def make_dir(s):
    dir = {}
    leng = len(s)
    for i in range(0, leng):
        if s[i] in dir:
            dir[s[i]].append(i)
        else:
            dir[s[i]] = [i]
    return dir

def longest_sub(s1, s2):
    letters = make_dir(s1)
    max = 0
    s2_len = len(s2)
    s1_len = len(s1)
    for i in range(0, s2_len):
        if s2[i] in letters:
            for l in letters[s2[i]]:
                tmp_max = 0
                it1 = l
                it2 = i
                while s1[it1] == s2[it2]:
                    tmp_max += 1
                    it1 += 1
                    it2 += 1
                    if it1 >= s1_len or it2 >= s2_len:
                        break
                if tmp_max >= max:
                    max = tmp_max

    return max

print(longest_sub('ooooooooooo','oooooooooooooooooo'))