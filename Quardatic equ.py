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
#Programe to find Area of Square, Reactangle, Circle, Traingle.
import cmath
print("Area calculation\n ")
cont='y'
while cont=='y' or cont=='Y' :
	print("Area of circle : 1 ")
	print("Area of square : 2 ")
	print("Area of reactangle : 3 ")
	print("Area of traingle : 4 ")
	choice=int(input("\nEnter your choice : "))
	if choice== 1 :
		r=int(input("Enterv radius : "))
		print("Area of circle = ", cmath.pi*r*r)
	elif choice==2 :
		s=int(input("Enter the side of square : "))
		print("Area of square = ", s*s)
	elif choice==3 :
		l=int(input("Enter the lenght : "))
		b=int(input("Enter the breath : "))
		print("Area of reactangle = ", l*b)
	elif choice==4 :
		a=int(input("Enter side 1 : "))
		b=int(input("Enter side 2 : "))
		c=int(input("Enter side 3 : "))
		s=(a+b+c)/2
		t=s*(s-a)*(s-b)*(s-c)
		print("Area = ", cmath.sqrt(t))
	else :
		print("Invalid choice ")
	cont=input("\nDo you want to continue ? (y/n) : ")
print("\nThankyou ")