numbers = input("Enter a list of numbers spaced between each: ")
items = numbers.split()
list1 = [eval(x) for x in items]

def indexOfSmallestElement(list1):
    print("The index of the smallest number is", list1.index(min(list1)))
    

indexOfSmallestElement(list1)
