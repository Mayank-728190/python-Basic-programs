num1=int(input("Enter a number1;"))
num2=int(input("Enter a number2;"))
operator=input("Enter operator:")
# using match operator to form a calculator
match operator:
    case"+":
        print("Sum is",num1 +num2)
    case"-":
        print("Difference is ",num1-num2)
    case"*":
        print("product is ",nun1*num2)
    case"/":
        print("quotient is ",num1/num2)
    case _ :
        print("Enter a valid operator")