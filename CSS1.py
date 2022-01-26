#QUESTION-1
print('Write any three numbers to find its average.')
num1=float(input('Type your number here= ')) #Getting input for numbers...
num2=float(input('Type your number here= '))
num3=float(input('Type your number here= '))
avg=(num1+num2+num3)/3  #avg=average
print('The average of the typed in numbers is',avg)

#QUESTION-2
print("To compute a person's income tax.")
print("Tax Rate=20%.")
print("Person will get $10000 as a standard deduction.")
print("And $3000 as additional deduction for each dependent.")
gic=float(input('Type in the persons Gross Income here= ')) #gic= Gross income
nod=int(input('Type in the number of people dependent on the person= ')) #nod=number of dependents
sd=10000 #sd= standard deduction
ad=3000 #ad= additional deduction
dd=ad*nod #dd= dependent deduction
ti=gic-sd-dd #ti= taxable income
tax=(ti*20)/100
print("The person has to pay", tax,"as tax.") 

#QUESTION-3
print("Student[SID,Name,Gender,Course Name,CGPA]")
name=input('Name of student= ')
gender=input('Gender= ')
sid=int(input("SID= ")) 
cn=input('Course Name= ') #cn=Course Name
cg=float(input("CGPA= ")) #cg=CGPA
student=sid,name,gender,cn,cg #assinging all the input values to a variable...
print(student)

#QUESTION-4
print('Type down numbers of 5 students.')
num1=int(input("Numbers of Student-1= ")) #Assingning values of numbers to the variables..
num2=int(input("Numbers of Student-2= "))
num3=int(input("Numbers of Student-3= "))
num4=int(input("Numbers of Student-4= "))
num5=int(input("Numbers of Student-5= "))
num=(num1,num2,num3,num4,num5)
print(num)

#QUESTION-5
color=['Red','Green','White','Black','Pink','Yellow']
print(color)
#PART-A
del color[3]
print('After Deleting 4th item, new list is=', color)
#PART-B
color=['Red','Green','White','Black','Pink','Yellow']
color[3]=color[4]='Purple'
print('After replacing Black and Pink with Purple the result is=', color[0:4]+color[5:])
