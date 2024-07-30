n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
if n1>n2:
    #func
    small=n2 
    large=n1 

elif n1<n2 :
    #
    small=n1 
    large=n2 
else :
    print("gcd is",n1 )
temp=0
#small , large defined
for i in range(1,small+1):
    rem=large%i #1,2,3,4,6,12
    rem1=small%i#1,2,3,4,6,12
    if rem ==0 and rem1==0:
        temp=i    
print(temp)


    