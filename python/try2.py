#Write a Program to create a file called “Input.txt”, initialize it with a
#string of your choice and perform the read operation to read only the first
#3 characters from the file.
file = open("input.txt", "w")
str=input("Enter a string :")
if str!="" and str.isdigit()==False:
    for i in range(len(str)):  
        file.write(str[i])
else:
    print("INVALID INPUT !!!!")
file.close()
file2=open("input.txt","r")
m=file2.readlines()
print(m)
file.close()
file3=open("input.txt","r")
n=file3.read(3)
print(n)
file3.close()