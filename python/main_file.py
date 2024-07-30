#error checking condition for a integer
a=input("Enter an integer:")
b=input("Enter second integer:")
if a !="" and a.isdigit()== True:
    if b!="" and b.isdigit()== True:
        #do something
        num1=int(a)
        num2=int(b)
    else : 
        print("Invalid Input")
else:
    print("Invalid Input")

#extracting a particular the string from the given string
str1=int("Enter the String:")
str2=str1[2:45]
print(str2)

#finding the length of the string
print(len(str1))

#import math
#ceil(n) in python is an inbuilt math function in Python that returns the smallest integer number which is greater than or equal to n
''' functions of math lib
math.sqrt(a)
math.factorial(b)
math.power(a,b)-->a^b
'''
#even odd
a=int(input("Enter a number:"))
if a%2==0:
    print("even number")
else:
    print("odd number")


#palindrome
str=input("enter a string:")
if list(str)==list(str[::-1]):
    print("palindrome")
else:
    print("Not a palindrome")

# method to compute gcd ( Loops )

def computeGCD(x, y):

	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small + 1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i
			
	return gcd

a = 60
b = 48

# prints 12
print ("The gcd of 60 and 48 is : ", end="")
print (computeGCD(60,48))

#Armstrong Number
digit=len(str)
while str>0 :
    rem =str%10
    sum=sum+(rem**digit)


#making user factorial function
def fact(n):
    if (num<2):
        return 1
    return num*fact(n-1)

#fibonacci 
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num=10
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")

list = []
tuple = ()
array==list
deleted_item = array.pop(position)
#position== indexing ->0,1,2,3, 
#filter function
array=list(filter(lambda x:int(x),main_list))
#lambda is used to find all the divisors of x or something like that in the following list
#lambda x:x%5==0  -> divisors of 5 in the list
#lambda x:x>9  -> numbers greater than 9

#Data Handling
'''file=open("name.txt",r or w or a )
 reading a file
 file.read()
 file..write("Mayank")

import numpy as np 
array=np.array([1,2,3,4])

 sliced array 
 arr_1=arr[1:3]
 indexing hogi : 0,1,2,3,4,5....
 ismein 1 include hoga and 3 rd index exclude hota Hai 

 printing the array 
print(arr_1)
dimension depends on the number of pairs of square brackets in arr_1

sorting the array
arr_2=np.sort(arr)
concatenation of the array 
arr_3=np.concatenate(arr1,arr2)3 matlab jodna array ko

Dimensionality check
array=np.array([1,2,3,4])
Dimensionality=array.ndim

Pandas
import pandas as pd 
data={
    "rollno":[],
    "name":[]
}
df=pd.DataFrame(data)
print(df)'''