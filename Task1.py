# Create a Boolean variable named x
x = bool(input())
print(x)

# Create an integer variable named y
y = int(input())
print(y)

# Create a float variable named z
z = float(input())
print(z)

# Create a string variable names s
s = input('')
print(s)

# Convert the int variable to float
# multiply the integer by 1.0
y = 10*1.0
print(y)

# Can we convert the str to int ?
# by adding int before input   
int(input())

# Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]

# Create a tuple from 10 to 15
t = (10,11,12,13,14,15)

# Convert the list to tuple
numbers = (1,2,3,4,5)

# Create a dict of 3 values
employee = {
    'name'    : "Radwa",
     "age"    : 29   ,
     "salaly" : 35006
}

# Can we use semi colon ; with python
# semicolons can be employed in Python to separate multiple statements on a single line but it is not commonly used.

# Python is interpreted or compiled ?
#  interpreted language

# What is the differences between low level & high level
# High-level languages are often used for software development, web development, and database management, Low-level languages are typically used for system programming, device driver development, and embedded systems

# What is the differences between = , ==
# = used for variables     == mean equal in if condition

# What do we mean by using !=
# not equal in if condition

# What is the operator precedence
# +  -  *  /  %

#Create a variable x with value of 10
x = 10

# Increase x value by 15 using assignment operators
x = 10+15

# Divide the x value by 5 using assignment operators
x = 10/5

# Multiply the x value by 10 using assignment operator
x = 10*10

# Get module of x on 3 using assignment operators
x = 10%3

# Using python print the module of 11 to 4
y = 11%4
print(y)

# Print the exponent of 2,3
z = 2**3

# Divide 11 by 3 using python division
y = 11/3

#Can we divide 11 by 3 and get an integer number ?
# NO

# Check if 10 is bigger than 15 or not
#  If 10 is not bigger than15 print x is smaller than 15
x = 10
y = 15
if x>y:
    print(True)
else:
    print("x is smaller than 15")

# In which cases we will use all
# What is the differences between all , and
# What is the differences between any , or
#?????????????????????????

# What is the differences between if , elif
#"if" is used for single condition testing, while "if-elif" allows you to check multiple conditions in a sequence

#What is the differences between elif else
#the difference is that the code always checks to see if an 'if' statement is true, checks 'elif' statements only if each 'if' and 'elif' statement above it is false, and 'else' runs only when the c


# Can we use more than one elif 
# Yes

#Can we use more than one else
# No

# write s simple ternary operator
# ??????????

# in elif , python will check all the conditions no matter what ?
# Yes

# in elif we use else for ... ?
# to end the condition

# if we have this list [2,4,6,8,10] :
# check to see if 4 in this list or 
# check to see if 4 and 6 in this list on not
# check to see if 3 or 6 in this list
# check to see if 2 , 4 and 5 in this list
numbers = [2,4,6,8,10]
if 4 in numbers:
    print(4)
elif    4 and 6 in numbers:
    print(4,6)
elif 3 or 6 in numbers:
    print(3) or print(6) 
else:
    print(False)
    #???????????????صح و لا لا 
       