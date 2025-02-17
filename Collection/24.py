row0= input("Enter a 3-by-4 matrix row for row 0: ")
items = row0.split()
row1= input("Enter a 3-by-4 matrix row for row 1: ")
items1 = row1.split()
row2= input("Enter a 3-by-4 matrix row for row 2: ")
items2 = row2.split()
list1 = [eval(x) for x in items]
list2 = [eval(x) for x in items1]
list3 = [eval(x) for x in items2]

matrix = [list1, list2, list3]

def sumColumn(matrix):
    for column in range(len(matrix[0])):
        total = 0
        for row in range(len(matrix)):
            total += matrix[row][column]
        print("Sum of the elements for column", column, "is", float(total))

sumColumn(matrix)
