'''def fibo(limit):
    a=0
    b=1
    while a<=limit:
        print(a,end="  ")
        a,b=b,a+b
        
limit= int(input("Enter a number:"))
fibo(limit)
n =int(input("number:"))
if n%4==0 and n%100!=0:
    print("leap year")
else:
    print("not a leap year")'''


list1=[1,2,3]
list2=[3,9,6]
list3=list1+list2
print(list3)
list4=[]
for i in range(0,3):
    value=list1[i]+list2[i]

    list4.append(value)
    
print(list4)
list4.sort()
print(list4)