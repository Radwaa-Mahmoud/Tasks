# Q.1 write  a program to display only those numbers from list
# the number must be divisible by five.
#if the number is greater than 150,then skip it and move to the next numx+=1ber
#if the number is greater than 500, then stop the loop 
numbers = [12,75,150,180,145.525,50]
for num in numbers:
    if num > 500:
        break
    if num %5==0:
        if num > 500:
            continue
        print(num)



# Q.2 write a program to count the total number of digits in a number using a while loop.
number = 75869
x = 0
while number !=0:
    number //= 10 
    x += 1
print(x)    


# Q.3 reverse the numbers
list1 = [10,20,30,40,50]
for i in (list1[::-1]):
    print(i)


# Q.4 Display numbers from -10 to -1 using for loop.
for i in range(-10,0):
    print (i)

# Q.5 write a program to print multiplication table of a given number
# for example , num=2
num = int(input("Enter the number :"))
for i in range(1,11):
    print(i*num)

# Q.6 display fibonacci series up to 10 terms
# the first two numbers are 0 and 1
term = int(input("how many terms: "))   
num1 = 0 
num2 = 1
count = 0
while count<term:
    if count <=1:
        x=count
    else:    
        x = num1+ num
        num1=num2
        num2=x
    print(x)
count= count+1
#بيطلع اصفار معايا و مش عارفه اضبط الكود كويس 