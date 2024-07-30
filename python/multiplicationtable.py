sankhya=input("enter the sankhya to find its multiplication table =")
sankhya2=input("enter the sankhya to which it should multiply=")
if sankhya!="" and sankhya.isdigit()==True:
    if sankhya2!="" and sankhya2.isdigit()==True:
        num=int(sankhya)
        print("the multiplication table of",num,"is-")
        i=1
        while i<=int(sankhya2):
            mul=(num*i)
            print(num,"x",i,"=",mul)
            i+=1       
    else:
        print("Invalid input hai boss ! integer value daalo...")  
else:
    print("Invalid input hai boss ! integer value daalo...")        
        
