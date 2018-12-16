

def prettyPrint(n):
    tab=[[0 for j in range(n*2-1)] for i in range(n*2-1)]
    for j in range(n):
        for i in range(j,n*2-j-1,1):
            tab[i][j] = str(n-j)
            tab[j][i] = str(n-j)
            tab[-1-j][i] = str(n-j)
            tab[i][-1-j] = str(n-j)

    for i in range(n*2-1):
        print(''.join(tab[i]))



prettyPrint()

