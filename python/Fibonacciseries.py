#FIBONAACCI SERIES - 0 1 1 2 3 5 8 13 21 ......
limit=input("enter the value of n till which u want to see the series= ")
print("0 1 ",end=" ")
num1=0
num2=1
num3=1
nextno=num2
if limit!="" and limit.isdigit()==True:
    temp=int(limit)
    while nextno<= temp :
        print(nextno,end="  ")
        
        num1,num2=num2,nextno
        nextno=num1+num2
    print()   
else:
    print("INAVLID INPUT HAI BOSS ! integer value daalo ")
    