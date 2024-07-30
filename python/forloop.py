#for loop
for i in range(1,11):
    print(i,"Hello world")
    
for j in range(0,11,2):
    print(j)
#Pattern ques1
n=int(input("Enter a number:"))
for i in range(n):
    for j in range (1,n+1):
        print(j,end="")
    print()
    
    
for k in range(n):
    for l in range(1,k+1):
        print(l,end="")
    print()
    
    
    
for m in range(n+1):
    print(" "*(n-m),end="")
    for p in range(1,2*m):
        print(p,end="")
    print()