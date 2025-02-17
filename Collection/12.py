number1 = input("Enter your first integer: ")
number2 = input("Enter your second integer: ")
number3 = input("Enter your third integer: ")

if number1>number2 and number1>number3 and number2>number3:
    print(number3, number2, number1)
elif number2>number1 and number2>number3 and number1>number3:
    print(number3, number1, number2)
elif number2>number1 and number2>number3 and number3>number1:
    print(number1, number3, number2)
elif number3>number1 and number3>number2 and number2>number1:
    print(number1, number2, number3)
elif number3>number1 and number3>number2 and number1>number2:
    print(number2, number1, number3)
elif number1>number2 and number1>number3 and number3>number2:
    print(number2, number3, number1) 
