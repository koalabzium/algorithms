arr = ['3','30','34']
s = '3'
def findMaxLen(arr):
    max = len(arr[0])
    for i in arr:
        len = len(i)
        if len(i) > max:
            max == len
    return max

def cmp(a,b):
    i = 0
    a += '.'
    b += '.'
    while a[i] != '.' or b[i] != '.':
        if a[i] != '.' and b[i] == '.':
            if a[i-1]>b[i]:
                return -1
            else:
                return 1
        if b[i]!='.' and a[i]=='.':
            if b[i-1]>a[i]:
                return 1
            else:
                return -1
        if int(a[i]) > int(b[i]):
            return 1
        elif int(b[i]) > int(a[i]):
            return -1
        elif int(a[i]) == int(b[i]):
            i += 1
    return 0

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

print(sorted(arr,key = cmp_to_key(cmp)))
print(cmp('3','30'))
