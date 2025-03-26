# check the given number is positive or negative
num1 = int(input('enter a number'))
if num1>0:
    print('positive')
else:
    if num1==0:
        print('zero')
    else:
        if num1 == -1:
            print('-1')
        else:
            print('Negative')

# 2)check the given numer is even or odd
A = int(input('Enter a Number'))
if A%2==0:
    print('The Given Number is even')
else:
    print('The given number is odd')

# 3)check the person is eligible to vote
age = 18
if age>18:
    print('The Person is eligible to vote')
else:
    print('The person is not eligible to vote')

# 4)check the greater number
A = int(input('Enter a Number:'))
B = int(input('Enter a Number:'))
if A>B:
    print(A, "is greater than ",B)
else:
    print( B ,'is greater than',A)

# 5)Pass or Fail

A = int(input('Enter your marks:'))
if A > 40:
    print('Pass')
else:
    print("Fail")

# 6)print the week based on given number
A = int(input('Enter the number of your week:'))
if A == 1:
    print('Monday')
elif A == 2:
    print('Tuesday')
elif A == 3:
    print('Wednesday')
elif A == 4:
    print('Thursday')
elif A == 5:
    print('Friday')
elif A == 6:
    print('Saturday')
else:
    print('Sunday')

# 7)simple Calculator
A = int(input('Enter your first Number:'))
B = int(input('Enter your Second Number:'))
C = input('enter the operator:')
if C== '+':
    print(A + B)
if C== '-':
    print(A - B)
if C== '*':
    print(A * B)
if C== '/':
    print(A / B)

# 8)print the month based on number
A = int(input('Enter a number of the month you required:'))
if A == 1:
    print('January')
elif A == 2:
    print('February')
elif A == 3:
    print('March')
elif A == 4:
    print('April')
elif A == 5:
    print('May')
elif A == 6:
    print('June')
elif A == 7:
    print('July')
elif A == 8:
    print('August')
elif A == 9:
    print('September')
elif A == 10:
    print('October')
elif A == 11:
    print('November')
else:
    print('December')

# b 1)
A = int(input('Enter the first number:'))
B = int(input('Enter the second number:'))
C = int(input('Enter the Third number:'))
if A>B and A>C:
    print(A,'is greater than', B,C)
if B>C and B>A:
    print(B,'is greater than',A,C)
if C>A and C>B:
    print(C,'is greater than',B,C)

# b 2)
A = int(input('Enter a year:'))
if A%4==0:
    if A%100==0 or A%400==0:
        print('It is a leap year')
    else:
        print('it is not aa leap year')
else:
    print('Not a leap year')

# b 3)
A = input('enter a name:').lower()
for i in A:
    if i=='a' or i=='e' or i=='i'or i=='o'or i=='u':
        print ('The given name has vowels')
    elif i=='b' or i=='c' or i=='d'or i=='f' or i=='g' or i=='h' or i=='j' or i=='k' or i=='l' or i=='m' or i=='n' or i=='p' or i=='q' or i=='r' or i=='s' or i=='t' or i=='v' or i=='w' or i=='x' or i=='y' or i=='z':
        print('it is a consonant')
    else:
        print('neither')

# b 4)
Marks = int(input('Enter your marks:'))
if Marks>=90 or Marks >=100:
    print('Grade A')
elif Marks>=80 or Marks>=89:
    print(('Grade B'))
elif Marks>=70 or Marks>=79:
    print('Grade C')
elif Marks<70:
    print('Fail')

# b 5)
a = int(input('Enter a Number'))
b = int(input('Enter a Number'))
c = int(input('Enter a Number'))

if a+b>c and b+c>a and c+a>b:
    print('The Sides form a valid triangle')
else:
    print('The sides donot form a valid triangle')


# print all numbers from 1 to 100
for i in range(1,101):
  print(i)
    
# write a program to print sum of first n natural numbers 
N = int(input('Enter a number:'))
if N<0:
    print('Enter a valid number')
else:
    sum = (N*(N+1))/2
    print(sum)

# Q :print all the even numbers between 1 and 50
num = 1
while num<=50:
    if num%2==0:
        print(num)
    num+=1


# To display the multiplication table of a given number.first 20
A = int(input('Enter a number'))
product = 1
for j in range(1,21):
        product = A * j
        print(A ,'*', j ,'=', product)


# fibonacci series
a = 0
b = 1
c = 0
num = 0  
print(a)
print(b)
for i in range(2,11):
    c = a + b
    print(c)
    a=b
    b=c
    num+=1

# check if the given number is prime or not

A = True
num = int(input('enter a number:'))
for i in range(2,num):
    if num % i == 0:
        print('The given number is not a prime')
        A = False
        break
else:
    if A:
        print('The given number is prime')

# factorial using while loop 
num = 1
fact=1
while (num<=5):
    fact = fact*num
    print(fact)  
    num+=1  


# Numbers that are divisible by both 3 & 5
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)


# table of a given number
A = int(input('enter a number'))
for i in range (1, A+1):
    for j in range(1,11):
        multiply = i * j
        print(i ,'*', j ,'=', multiply)



# reverse number
A = 54312
reverse=0
count = 0
sum1=0
while A>0:
    rem = A%10
    # print(rem)
    reverse = reverse*10+rem
    if rem%3==0:
        print(rem)
    sum1=sum1+rem
    A = A//10
    count=count+1
print(sum1)
print(count)