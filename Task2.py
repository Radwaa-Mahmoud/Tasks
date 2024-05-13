# Q8. write a program to calculate the electricity bill....
units =int(input('enter units = '))
if units <=100 :
    print('No charge')
elif 100 < units <= 200:
    cost = (units-100)*5
    print("Total cost =", cost)
else: 
    units > 200 
    cost = (units - 200)*10
    print("Total cost = " , cost+500)

# Q1.write a program to accept percentage....
Marks = int(input('Enter the degree ='))
if Marks > 90 :
    print('Grade = A')
elif 90<= Marks >80  :
    print ('Grade = B')
elif 80<= Marks >= 60 :
    print("Grade = C")
elif Marks <60 :
     print('Grade = D')
else:
     print("failed")     

 # Q2 the cost price of bike 
     cost = float(input("Enter the cost price ="))
if cost >100000 :
    print("Tax is", cost*0.15)  
elif   100000<= cost >50000  :
    print("Tax is", cost*0.1)
else:
    cost <= 50000
    print("Tax is" ,  cost*0.05)

# Q5. write a program to find the largest number out of two numbers........
num1 = float(input("Insert your number ="))  
num2 = float(input("Insert your number =")) 
print("the largest number is num 1") if num1>num2 else print("the largest number is num2")

# Q6. check whether a number is positive or negative 
x = int(input("Enter the number = "))
print('the number is positive') if x >= 1 else print("the number is negative")

# Q7 . number is even or odd
z = float(input("Enter the number : "))
print("even") if z%2==0 else print("odd")

# Q9 . find the largest number out of three numbers 
num1 = int(input("enter the number ="))
num2 = int(input('enter the number ='))
num3 = int(input("enter the number = "))
if num1>num2 and num1>num3:
    print('the largest number is num1')
elif num2>num1 and num2>num3:
    print('the largest number is num2')  
else:
    print('the largest number is num3')


# Q1  . calculate the percentage of classs attened
working_days =int(input("Enter the days of working ="))
absent_days =int(input("Enter the days of absence ="))
percentage = (working_days-absent_days)/working_days*100
print("you will not be able to sit in exam")if percentage<75 else print("you will be able to sit in exam")

# Q2. accept the percentage and disply the grade
percentage = float(input('Enter your percentage ='))
if percentage > 80 :
    print('Grade = A+')
elif 80<= percentage > 60  :
    print ('Grade = A')
elif 50<= percentage >= 60 :
    print("Grade = B+")
elif 50<= percentage >=45 :
     print('Grade = B') 
elif 45<= percentage >=25:
    print('Grade = C')
else:
     percentage <25
     print("Grade = D") 
