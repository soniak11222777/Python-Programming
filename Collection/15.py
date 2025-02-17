def reverse(number):
    reversed_num = 0
    while number !=0:
        d = number % 10
        reversed_num = reversed_num *10 + d
        number= number//10
    print(reversed_num)

number= eval(input("Enter an integer to be reversed: "))
reverse(number)

