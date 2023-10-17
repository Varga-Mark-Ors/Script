#!/usr/bin/env python3

def matgen():
    mat = [[0 for i in range(10)] for j in range(10)]
    return(mat)

def sakk(tabla):
    mat = matgen()
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if (i == 0) or (i == n-1):
                mat[i][j] = "-"
            if (j == 0) or (j == n-1):
                mat[i][j] = "|"
            if ((i == 0 or j == 0) and (i == n - 1 or j == n - 1)) or ((i == 0 and j == i) or (i == n - 1 and j == i)):
                mat[i][j] = "+"
            if (i > 0 and i < n -1) and (j > 0 and j < n - 1):
                mat[8 - tabla[j - 1]][j] = "Q"
            if mat[i][j] == 0:
                mat[i][j] = "."
    
    return(mat)      

def kiiras(tabla):
    n = len(tabla)
    for i in range(n):
        print()
        for j in range(n):
            print(tabla[i][j], end=" ")

def main():
    
    tabla=sakk([0,4,7,5,2,6,1,3])
    kiiras(tabla)


if __name__=="__main__":
    main()