score = []
value = input("Enter a list of numbers seperated by spaces: ")
score.append(value)
items = value.split()
list1 = [eval(x) for x in items]

average = sum(list1)/len(list1)
amount = 0
below = 0
    
for i in range(len(list1)):
    if list1[i] >= average:
        amount += 1
    if list1[i] < average:
        below += 1

print("The number of scores above or equal to the average is", amount)
print("The number of scores below the average is", below)
