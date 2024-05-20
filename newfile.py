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
s=input("Enter a string for palindrome : ")
pali(s)
#programto find a year is a leap year or not by function
def leap(y):
    if y%4==0 :
    	return "Yes",y," is a leap year"
    else:
    	return "No", y, " is not a leap year"
y=int(input("Enter the Year : "))
print(leap(y))
#programe to print fabonicca series (1, 1, 2, 3, 8, 13, 21,... n ) by function
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
n=int(input("Enter the number of terms for fabonicca series : "))
fab(n)
#programe to print right star pattern by function
def rightstar(n):
	for i in range(1,n+1):
		print(" "*(n-i),"*"*i)
n=int(input("Number of rows for right star pattern : "))
rightstar(n)
#programe to print multiplication table by function
def tab(n):
	for i in range(1,11):
		print(n,"X",i,"=",n*i)
n=int(input("Enter the number for table : "))
tab(n)
#programe to print star pyramids by function
def star(n):
	for i in range(1,n+1):
		print("*"*i)
n=int(input("Enter the numbers of rows for star pattern : " ))
star(n)
#programe to find the sum of series 1+1/1!+2/2!+3/3!..+n/n! by function
def sumOfSeries(num): 
    sum = 1
    fact = 1
    for i in range(1, num+1): 
        fact *= i 
        sum= sum + (i/ fact) 
    return sum
n=int(input("Enter the number of terms for add in series : "))
print("Sum: ", sumOfSeries(n))