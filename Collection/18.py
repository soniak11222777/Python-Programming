from random import randint

def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(randint(0, 1), end="")
        print("")
number = input("Enter n: ")
printMatrix(int(number))
