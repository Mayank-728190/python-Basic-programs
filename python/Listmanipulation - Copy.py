#Write a Program to create a two list and perform the following operation’s :
list1=[]
num1=input("enter the number of elements you want to put in the list1=")
if num1!="" and num1.isdigit()==True:
    n1=int(num1)
    for i in range(n1):
        element1=input("enter the elements in list1= ")
        list1.append(element1)
else:
    print("inavlid input...integer value do")
list2=[]
num2=input("enter the number of elements you want to put in the list2=")
if num2!="" and num2.isdigit()==True:
    n2=int(num1)
    for i in range(n2):
        element2=input("enter the elements in list2= ") 
        list2.append(element2)
else:
    print("inavlid input...integer value do")
print("list 1 is :",str(list1))
print("list 2 is :",str(list2))     
#1) Compare the contents of the two list.
list1.sort()
list2.sort()
if list1==list2:
    print("both the lists are equal! As the value on same index position is same ")
else:
    print("both the lists are not same")
#2) to find the number of the elements in the list.
#To count the number of elements in a string we use len() fucntion:
print("the number of elements in list1 is = ",len(list1))
print("the number of elements in list2 is = ",len(list2))
#3) Sort the elements of the list
print("List1 after getting sorted is -")
print(list1)
print("List2 after getting sorted is -")
print(list2)
#4) Reverse the contents of the List.
list1.reverse()
print("the list1 after reversing is - ")
print(list1)
list2.reverse()
print("the list2 after reversing is - ")
print(list2)
#5) Add the Elements of the two list:
add1=input("enter the value you want to add in the list1")
if add1!="" and add1.isdigit()==True:
    add=int(add1)
    list1.append(add)
else:
    print("invalid input.. integer value daalo")
print("list1 after adding the value",add,"is",list1)
add2=input("enter the value you want to add in the list2")
if add2!="" and add2.isdigit()==True:
    addin2=int(add2)
    list2.append(addin2)
else:
    print("invalid input .. integer value daalo")
print("list2 after adding the value",addin2,"is",list2)
print("Le chal gaya tera code jaa mauj kar ab :) ")



