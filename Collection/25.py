row0= input("Enter a 4-by-4 matrix row for row 1: ")
items = row0.split()
row1= input("Enter a 4-by-4 matrix row for row 2: ")
items1 = row1.split()
row2= input("Enter a 4-by-4 matrix row for row 3: ")
items2 = row2.split()
row3= input("Enter a 4-by-4 matrix row for row 4: ")
items3 = row3.split()
list1 = [eval(x) for x in items]
list2 = [eval(x) for x in items1]
list3 = [eval(x) for x in items2]
list4 = [eval(x) for x in items3]

matrix = [list1, list2, list3, list4]

def sumMajorDiagonal(matrix):
    diagonal = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if (i == j):
                diagonal += matrix[i][j]
    print("Sum of the elements in the major diagonal is", diagonal)

sumMajorDiagonal(matrix)
