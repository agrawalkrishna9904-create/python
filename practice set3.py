##1] WAP too ceck if a number even or odd
num=int(input("Enter some value:"))
if(num%2==0):
    print("num is even")
elif(num%2!=0):
    print("num is odd")


##2] WAP to find grratest of three numbers
a=int(input("enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))
if(a>b and a>c):
    print("num 1 id greater")
elif(b>=c):
    print("num 2 is greater")
else:
    print("num 3 is greater")


##3]WAP to check if number is multiple of 7 or not
num=int(input("Enter some num:"))
if(num%7==0):
    print("num is multiple of 7")
else:
    print("num is not multiple")