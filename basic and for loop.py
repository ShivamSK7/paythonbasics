# programe to print name
s=input("Enter your name : " )
print(s)
print("Hello" , s , ' ! ')
#programe to print age +20
a=int(input("Enter age : "))
print(a)
print(a+20)
#programe to print addition
a=int(input("Enter first number : " ))
b=int(input("Enter second number : " ))
print("Addition : " , a+b)
#peograme to print sum of natural numbers
n=int(input("Enter the number : " ))
sum=0
for i in range(1,n+1):
	sum=sum+i
print("Sum of first ",n,"natural numbers =",sum)
#programe to print multiplication table
n=int(input("Enter the number : " ))
for i in range(1,11):
	print(n,"X",i,"=",n*i)
#peograme to print factorial
n=int(input("Enter the number : " ))
fact=1
for i in range(1,n+1):
	fact=fact*i	
print("Factorial of" ,n , " = " ,fact)
#programe to print fabonicca series (1 1 2 3 8 13 21 )
n= int(input("Enter the number of terms : " ))
term1=1
term2=1
print(term1)
print(term2)
for i in range(3,n+1):
	term3=term2+term1
	print(term3)
	term1=term2
	term2=term3
#programe to print quardatic equation
import cmath
a=int(input("Enter the coefficient of a : "))
b=int(input("Enter the coefficient of b : "))
c=int(input("Enter the coefficient of c : "))
d=(b*b-4*a*c)
if d>0:
	r1=(-b+cmath.sqrt(d))/(2*a)
	r2=(-b-cmath.sqrt(d))/(2*a)
	print("Roots are real and unequal",r1,"and",r2)
elif d==0:
	r1=(-b)/(2*a)
	print("Roots are real and same ",r1)
else:
	print("No real roots are there ")
#programe to print addition of rendome numbers
n=int(input("How many numbers you want in list : " ))
list=[ ]
for i in range(n):
	list.append (int(input()))
sum=0
for i in list:
	sum=sum+i
print("Sum of list is : " ,sum)
#programe to print temprature convert calcius to feranhite
a=int(input("Enter the temprature in calcius :  " ))
print("Feranhite : ",(a*9/5)+32)
#programe to print temprature convert feranhite to calcius
a=int(input("Enter the temprature in feranhite : " ))
print("Calcius : ",	(a-32)*5/9)
#programe to print Sum 10 rendom number 
sum=0
for i in range(0,10):
	n=int(input("Enter a number : "))
	sum=sum+n
	print("Addition of numbers : " ,sum)
# prigrame to print Star pattern
n=int(input("Enter the numbers of rows : " ))
for i in range(1+n+1):
	print("*"*i)
#programe to print Nested loop
n=int(input("Enter the number of terms :"))
for i in range(0,n):
	print("A")
	for j in range(0,n):
		print(" J over")
print("Complete")
#programe to print Addition of rendome numbers  n
n=int(input("How many numbers you want in list : " ))
list=[ ]
for i in range(n):
	list.append(int(input()))
	sum=0
for i in list:
	sum=sum+i
print("Sum of list is : " ,sum)
#programe to print right star pattern
n=int(input("Number or rows : "))
for i in range(1,n+1):
	print(" "*(n-i),"*"*i)
# programe to print doller  ($) pettern
n=int(input("Enter the number of rows : "))
print("$"*n)
for i in range (2,n):
	print("$"," "*(n-4),"$")
print("$"*n)
# Programe to print prime numbers from 2to n
n=int(input("Enter a Number : "))
for i in range(2,n+1):
	for j in range(2,i+1):
		if i%j==0:
			print(i,"=",j,"*",int(i/j))
			break
		elif j == i-1 :
			print(i,"is a prime number ")
			break
