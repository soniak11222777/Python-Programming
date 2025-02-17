from random import randint

def printMatrix(n):
    matrix=[]
    for row in range(n):
        a=[]
        for column in range(n):
            a.append(randint(0,1))
            matrix.append(a)
printMatrix(2)

