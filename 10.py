name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
grossPay= payRate*10
federalTax = eval(input("Enter federal tax withholding rate: "))
total1 =  grossPay*federalTax
stateTax = eval(input("Enter state tax withholding rate: "))
total2 = eval(format(grossPay*stateTax, ".2f"))
total3 = total1+total2
total4 = grossPay - total3

print("Employee Name: " + name)
print("Hours Worked: " + format(hours, ".1f"))
print("Pay Rate: $" + str(payRate))
print("Gross Pay: $" + str(grossPay))
print("Deductions: \n \t Federal Withholding (" + str(federalTax*100) + "%): $" +str(total1)+ "\n \t State Withholding (" +str(stateTax*100)+ "%): $" +str(total2)+ "\n \t Total Deduction: $" + str(total3))
print("Net Pay: $" + str(total4))

    
