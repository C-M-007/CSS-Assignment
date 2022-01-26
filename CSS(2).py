#QUESTION-1

x="Python is a case sensitive language."
#part-(a)-- To find Length of any string we use function len().
print(len(x))
#part-(b)-- To reverse the order in one line code we can use string slicing.
print(x[::-1])
#part-(c)-- To store string in a new string.
y=x[10:26] # Where y is the new string.
print(y)
#part-(d)-- To replace some part of the string.
print(x.replace("a case sensitive", "object oriented"))
#part-(e)-- To find index of substring "a".
print(x.find("a"))
#part-(f)-- to remove the spaces from the string.
print(x.replace(" ",""))


#QUESTION-2

# Storing the SID,Name,Branch and CGPA in variables through input by user.
a=str(input("Whats your name:"))
b=int(input("Enter Your SID:"))
c=str(input("Enter your Branch:"))
d=float(input("Enter your CGPA:"))
print("Hey ,",a,"Here!")
print("My SID is",b)
print("I am from",c,"department and my CGPA is",d)


#QUESTION-3

#Calculate with the help of bitwise operators
a=56
b=10
#part-(a)
print(a&b)
#part-(b)
print(a|b)
#part-(c)
print(a^b)
#part-(d)
print(a<<2)
print(b<<2)
#part-(e)
print(a>>2)
print(b>>4)


#QUESTION-4

#To find the greatest of three numbers entered by the user.
num1=float(input("Enter your 1st number here:"))
num2=float(input("Enter your 2nd number here:"))
num3=float(input("Enter your 3rd number here:"))
#Using if-else statements
if(num1>=num2) and (num1>=num3):
    large=num1   #large=largest number.
elif(num2>=num3) and (num2>=num1):
    large=num2
else:
    large=num3
print("The largest number is",large)    


#QUESTION-5

#To check whether the name is present in the string.
enter=str(input("type: "))
if "name" in enter:
    print("Yes")
else:
    print("No")


#QUESTION-6

#To check whether the input sides can form a triangle or not.
side1=int(input("Type down the first side:"))
side2=int(input("Type down the second side:"))
side3=int(input("Type down the third side:"))
if((side1+side2 >side3) and (side2+side3 >side1) and (side3+side1 >side2)): 
    print("Yes,These sides can form a triangle.")
else:
    print("No,These sides cannot form a triangle.")
    







