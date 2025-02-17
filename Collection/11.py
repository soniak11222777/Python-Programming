import random
number1 = random.randrange(0,100)
number2 = random.randrange(0,100)
question = eval(input("What is "+ str(number1)+ " plus "+ str(number2)+ "?: "))
print("That answer is", number1 + number2 == question, "!")

