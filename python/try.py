#Using Filter function, write a program to display multiple of 5 from a given array.


numbers=[]
num1=input("enter the number of elements you want to put in the list1=")
if num1!="" and num1.isdigit()==True:
    n1=int(num1)
    for i in range(n1):
        element=input("enter the elements in list1= ")
        numbers.append(element)
else:
    print("invalid input")


arr_filter = list(filter(lambda x: int(x)%5==0,numbers))
print("Filtered list:", arr_filter)