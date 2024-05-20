# programe to check Palindrome word
c='y'
while c=='y':
	s=input("Enter a string : ")
	#case senstive
	if s == s[ : : -1 ]:
		print("\ncase - senstive compresion : String is a Palindrome ")
	else :
		print("\ncase - senstive comprasion : string is not a Palindrome  ")
	# case insenstive 
	if s.upper () ==s[ : : -1 ].upper():
		print("\ncase - ignore comreasion : Palindrome ")
	else :
		print("\ncase - ignore compresion : not a Palindrome ")
	c=input("\nContinue ? (y/n) : ")
#programe to print quardatic equation using while loop
c='y'
while c=='y' :
	import cmath
	a=int(input("Enter the cofficent of x**2 : "))
	b=int(input("Enter the cofficent of x : "))
	c=int(input("Enter the constent : "))
	d=b*b-4*a*c;
	if d>0:
		r1=(-b+cmath.sqrt(d))/(2*a)
		r2=(-b+cmath.sqrt(d))/(2*a)
		print("Roots are real and unequal",r1,"and",r2)
	elif d==0:
		r1=-b/2*a
		print("Roots are real and same ",r1)
	else:
			print("No real roots are there ")
	c=input("\nContinue ? (y/n) : ")