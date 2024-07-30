#Write a Program to create a file called “Input2.txt”, perform the 
#write/read operation in it with a string “Computer Science”.
str="Computer Science"
file = open("input2.txt", "w")
for i in range(len(str)):  
        file.write(str[i])
file.close()
file2 = open("input2.txt", "r")
n=file2.read()
print(n)
file2.close()