#demo1
def fnDemo1():
	print("Functions")
fnDemo1()
print("Done")
#demo2
def fnDemo2(str):
	print("Hello",str)
fnDemo2("Jack")
str=input("Enter name : ")
fnDemo2(str)
#area of quardilaterel
def areaSquare(side):
	return side*side
def areaRect(l,b):
	return l*b
side=int(input("Enter side of square : "))
print("Area = ",areaSquare(side))
l,b=input("Enter length & breath ").split( )
l=int(l)
b=int(b)
print("Area = ",areaRect(l,b))
#addition
def add(a,b,c):
	s=a+b+c
	return s
a=0
b=0
c=0
a,b,c=input("Enter three numbers : ").split()
print("Sum = ",add (a,b,c))
#sum of values
def sum(*args):
	s=0
	for i in args :
		s+=i
	print(s)
sum(1,2,3)
sum(4,5,6,7,8)
sum()
def showValues(*vargs):
	for v in vargs:
		print(v)
showValues("Single Value ")
showValues("Multiple ","Values")
showValues(10,20,30,40)
#programe to print cube of a number by function
def cube(n):
	c=n*n*n
	return c
n=int(input("Enter a number for cube : "))
print("Cube = ",cube(n))
#programe to print temp from faranhit to calcius by function
def farconv(n):
	c=(n-32)*5/9
	return c
n=int(input("Enter the temp. into faranhite : "))
print("Celcius = ",farconv(n))
#programe to print temp from calcius to faranhit by function
def calsconv(n):
	f=(n*9/5)+32
	return f
n=int(input("Enter the temp. into calcius : "))
print("Faranhit = ",calsconv(n))
#programe to print factorial by function
def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
n=int(input("Enter the number for factorial : "))
print("Factorial = ",fact(n))
# programe to check Palindrome word by function
def pali(s):
		#case senstive
		if s == s[ : : -1 ]:
			print("\ncase - senstive compresion : String is a Palindrome")
		else :
			print("\ncase - senstive comprasion : string is not a Palindrome  ")
		# case insenstive 
		if s.upper () ==s[ : : -1 ].upper():
			print("\ncase - ignore comreasion : Palindrome ")
		else :
			print("\ncase - ignore compresion : not a Palindrome ")
s=input("Enter a string : ")
pali(s)
#programto find a year is a leap year or not by function
def leap(y):
    if y%4==0 :
    	return "yes"
    else:
    	return "no"
y=int(input("Enter the Year : "))
print(leap(y))
#programe to print fabonicca series (1 1 2 3 8 13 21 ) by function
def fab(n):
	term1=1
	term2=1
	print(term1)
	print(term2)
	for i in range(3,n+1):
		term3=term2+term1
		print(term3)
		term1=term2
		term2=term3
n=int(input("Enter the number of terms : "))
fab(n)
#programe to print right star pattern
def rightstar(n):
	for i in range(1,n+1):
		print(" "*(n-i),"*"*i)
n=int(input("Number or rows : "))
rightstar(n)
#programe to print multiplication table by function
def tab(n):
	for i in range(1,11):
		print(n,"X",i,"=",n*i)
n=int(input("Enter the number for table : "))
tab(n)
#programe to print star pyramids
def star(n):
	for i in range(1,n+1):
		print("*"*i)
n=int(input("Enter the numbers of rows : " ))
star(n)
#programe to find the sum of series 1+1/1!+2/2!+3/3!..+n/n! by function
def sumOfSeries(num): 
    sum = 1
    fact = 1
    for i in range(1, num+1): 
        fact *= i 
        sum= sum + (i/ fact) 
    return sum
n=int(input("Enter the number of terms: "))
print("Sum: ", sumOfSeries(n))
#programe to print maximum value by function
def Findmax(lst,n):
	m= lst[ 0 ]
	for i in range (1,n):
		if lst[ i ]>m:
			m=lst[ i ]
	return m
lst=[ ]
n=int(input("Enter the number of values : "))
print("Enter the values ")
for i in range(0,n):
	a=int(input(" : "))
	lst.append(a)
p=Findmax(lst,n)
print("\nMaximum value is : ",p)