#QUESTION 1

sen=str(input("Type in any String: ")) #sen= Sentence/String
list1=sen.split()  
dict={} 
if list1.__len__()==1: #To know whether the length of string is 1 or not.   
    for i in list1[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list1:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#QUESTION 2

mon30 = [4, 6, 9, 11]#Number of months having 30 days
mon31 = [1, 3, 5, 7, 8, 10, 12]#Number of months having 31 days
def inpdate():
    global day
    global month
    global year
    day = int(input("Please Enter The Day: "))
    month = int(input("Please Enter The Month: "))
    year = int(input("Please Enter The Year: "))
    if year>2025 or year<1800 or month<1 or month>12 or day<1 or day>31: #Restrictions of day,month,year
        print("Please Enter a Valid Date or month or enter a year between 1800 and 2025")
    if day > 28 and month == 2 and year%4 != 0: #In case of month is feburary and its not a leap year.
        print("Please enter a valid Date!")
        inpdate()
    elif ((day > 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)): #In case of month is feburary and its a leap year.
        print("Please enter a valid Date!")
        inpdate()
    elif day > 30 and month in mon30: #In case of a month having 30 days 
        print("Please enter a valid Date!")
        inpdate()
inpdate()
if day == 28 and month == 2 and year%4 != 0: #Feburary month not in leap year.
    day = 1
    month = 3
elif ((day == 28 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)): #Feburary month in leap year.
    day += 1
elif ((day == 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
    day = 1
    month = 3
elif day == 30 and month in mon30:  #For the end dates of month having 30 days.
    day = 1
    month += 1
elif day == 31: #For the end dates of month having 31 days.
    day = 1
    month += 1
else: #When any year ends.
    day += 1
if month == 13:
    month = 1
    year += 1
print("Next Date Is: ", day,'/',month,'/',year)


#QUESTION-3
nums=[2,5,7] 
res=[] #res here refers to an empty list
for i in nums: 
    answer=(i,i*i) #Here i have used answer as a tuple to store values of i and its square
    res.append(answer)#Here i have added the tuple to the res list defined previously
print(res)


#QUESTION 4

grade=int(input("ENTER YOUR GRADE BETWEEN 4 TO 10: "))
if(grade>10 or grade<4):
    print("PLEASE ENTER CORRECT GRADE")
elif(grade==4):
    print("Your Grade is 'D' and poor performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average performance")
elif(grade==7):
    print("Your Grade is 'B' and Good performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent performance")
else:
    print("Your Grade is 'A+' and outstanding performance")
print("\n")


#QUESTION 5

x = 6
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  
    print()
print("\n")

#QUESTION-6
'''Program to add student details in a dictionary and performing operations on that dictionary.'''

print("\n\tStudent Details Manager\n")

sid = int(input("Enter SID: ")) # taking input of name and sid from user
name = input("Enter Name: ")
students = {sid:name}

while True:
    wish = input("Do you want to enter another student details(Y or N): ").upper() #Ask whether to Enter details of another student or not
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input!!!')

#a-part

print("a." ,students)  #student details

#b-part

print("b." ,{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})   #sorting using names

#c-part

print("c." ,{k:v for k,v in sorted(students.items())}) #sorting using sid

#d-part

search = int(input("Please Enter SID Of The Student You Want To Search: " )) 
print("d. Student With The Given SID Is: " ,students[search])





#QUESTION 7
#FIBONACCI SERIES
#1,1,2,3,5,8,13,21,34,55....
def fibo(x):
   if x <= 1:
       return x
   else:
       return(fibo(x-1) + fibo(x-2))
n=int(input("Type in the number of terms that you want to be printed of Fabonacci series: ")) #n=number of terms.
if (n <= 0):    
   print("Please enter a positive integer!")
else:
   print("Final Fibonacci series is: ")
   sum=0
   for i in range(n):
       print(fibo(i))
       sum=sum+fibo(i)
avg=float(sum/n)
print("Average Of The final Fibonacci series = ",avg)


#QUESTION 8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# a-part

Set_1 = (Set1|Set2)-(Set1&Set2) #set of all elements that are in Set1 and Set2 but not both.

print("a. ", Set_1)

# b-part

Set_2 = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1)) #set of all elements that are in only one of the three sets Set1, 
#Set2 and Set3.

print("b. ", Set_2)

# c-part

Set_3= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3) #set of elements that are exactly two of the sets Set1, Set2 and Set3.

print("c. ",Set_3)

# d-part

Set_4 = set() #set of all integers in the range 1 to 10 that are not in Set1.
for i in range(1, 11):
    if i not in Set1:
        Set_4.add(i)
print("d. ", Set_4)

# e-part

Set_5 = set() #set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Set_5.add(i)
print("e. ", Set_5)
