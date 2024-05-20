#programe to find the sum of series 1+1/1!+2/2!+3/3!..+n/n! 
n=int(input("Enter the number  of terms : "))
sum = 1
fact = 1
for i in range(1, n+1):
        fact *= i 
        sum= sum + (i/ fact)
print("Sum : ",sum)
#programe to print ($ ) in square boundry 
n=int(input("Enter the number rows : "))
print("$"*n)
for i in range(2,n):
	print("$", " "*(n-4),"$")
print("$"*n)