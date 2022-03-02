#QUESTION 1

def hanoi_tower(n , fro , mid, to):
	if n == 0:
		return
	hanoi_tower(n-1, fro, mid, to)
	print("Move Disk ",n," from rod ",fro," to rod ",to)
	hanoi_tower(n-1, mid, to, fro)
n = 3
hanoi_tower(n, 'A', 'C', 'B')                #Calling TheFunction For 3 Disks
print("\n")


#QUESTION 2

#Part-A
#USING RECURSION

from tracemalloc import start
from math import factorial, remainder
n=int(input("Enter the number Of rows of The Pascal's Triangle: "))
print("Solving by Recursion Method...")            

def pascal_triangle(n,length = n):
    if n == 0:
        return
    pascal_triangle(n-1,length)
    print('  '*(length-n), end='')
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i      #Bionomial Coefficients
    print()
pascal_triangle(n)
print("\n")

#Part-B
#USING ITERATIONS(for/while loops)
print("Solving by Iterative Method...")           

from tracemalloc import start
from math import factorial, remainder
m=int(input("Enter number of rows for the pascal triangle:"))
for s in range(m):
    for x in range(m-s):
        print(end=" ")      #Assinging the spaces according to the design.....
    for x in range(s+1):
        print(factorial(s)//(factorial(x)*factorial(s-x)), end=" ")     #nCr = n!/r!*(n-r)!
    print()
print("\n\n")


#QUESTION 3

num1, num2 = map(int,input("Enter 2 Numbers: ").split())
Quotient = num1 // num2
Remainder = num1 % num2

#Part-a

print("Callability Check...")                          #Checking The Callability Of Quotient And Remainder
print(callable(Quotient))
print(callable(Remainder))

#Part-b

if (Quotient == 0):
    print("The Quotient Is Zero")
if (Remainder == 0):
    print("The Remainder Is Zero")
if (Quotient != 0 and Remainder != 0):
    print("All Values Are Non-Zero")

#Part-c

c_list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(c_list)):
    if c_list[i] > 4:
        result.append(c_list[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

#Part-d

setresult = set(result)
print("Set: ",setresult)

#Part-e

immutableSet = frozenset(setresult)                #Making The Set Immutable
print("Immutable set:",immutableSet)

#Part-f

print("Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")



#QUESTION 4

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("File Destroyed!")
stud1 = Student("Chiranjeev", 21104083)
print("File Created")
print(f"The name Of the student is {stud1.name} and SID is {stud1.roll_no}.")
del stud1
print("\n")


#QUESTION 5

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
emp1 = Employee("Mehak", 40000)     #emp-employee
emp2 = Employee("Ashok", 50000)
emp3 = Employee("Viren", 60000)

#Part-a

emp1.salary = 70000
print(f"The Updated Salary Of {emp1.name} Is {emp1.salary} ")

#Part-b

print("Record Of Viren Deleted!", end='')
del emp3
print("\n")


#QUESTION 6

word1 = input("Enter Any Word: ")
word1 = word1.lower()
word2 = input("Enter A New Word Using The Exact Same Letters: ")
word2 = word2.lower()
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
def userinput():
    if count_in_dict(word1) != count_in_dict(word2):
        print("The Words Aren't Matching, Friendship Is Fake!")
        return
    ans = input("Does The Word Makes Any Sense?(Y Or N) ")
    if ans == 'y' or ans=='Y':
        print("Passed The Friendship Test!!!")
    elif ans == 'n' or ans=='N':
        print("Meaningless Word , Friendship Is Fake!")
    else:
        print("Invalid Input,Try Again! ")
        userinput()
userinput()
