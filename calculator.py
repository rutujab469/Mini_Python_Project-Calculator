#mini project - Calculator
# 3 steps to build calculator:
      #1.function for operation
      #2.user input
      #3.print result

#step1: function for operation
#fuction to add two number:
def add(num1,num2):
    return num1+num2
#fuction to subtract two number:
def sub(num1,num2):
    return num1-num2
#fuction to muliply two number:
def multiply(num1,num2):
    return num1*num2
#fuction to divide two number:
def divide(num1,num2):
    return num1/num2
#fuction to avrage two number:
def avg(num1,num2):
    return (num1+num2)/2

#step2:user input
print("Please select operation:\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n"
      "5. Average\n")
select=int(input("select the operation from 1,2,3,4,5:"))
number1=int(input("enter first number:"))
number2=int(input("enter second number:"))

#step3:print the result
if select == 1:
    print(number1, "+", number2, "= " ,add(number1,number2))
elif select ==2:
    print(number1, "-", number2, "= " ,sub(number1,number2))
elif select ==3:
    print(number1, "*", number2, "= " ,multiply(number1,number2))
elif select ==4:
    print(number1, "/", number2, "= " ,divide(number1,number2))
elif select ==5:
  print("(", number1, "+", number2, ")", "/", "2", "=", avg(number1, number2))
else:
    print("Invalid operation!Please select again")
