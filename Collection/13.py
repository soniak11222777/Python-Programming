data = eval(input(" Enter an integer, the input ends if it is 0:"))

total=0
positives=0
negatives=0
count=0

if data==0:
      print("You didn't enter a number")
      count=0
      total=0
      positives=0
      negatives=0
else:
    while data!=0:
        total+=data
        count+=1
        if data>0:
            positives+=1
        else:
            negatives+=1
        data = eval(input(" Enter an integer, the input ends if it is 0:"))
    print ("The number of positives is", positives,"\nThe number of negatives is", negatives, "\nThe total is", total,"\nThe average is", float(total/count)) 

