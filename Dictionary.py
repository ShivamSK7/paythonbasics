#programe to print cube of a number
count='y'
while count=='y' or count=='Y' :
	d=dict ( )
	n=int (input("Enter the number of terms of cube : "))
	for i in range(1,n+1):
		d[i]=i*i*i
	print(d)
	count=input("\nContinue ? (y/n) : ")
# programe to count frequency of vowels using dictonery
c='y'
while c=='y' :
	acount=0
	ecount=0
	icount=0
	ocount=0
	ucount=0
	vowels={"a": acount,"e": ecount,"i": icount,"o": ocount,"u": ucount}
	str=input("Enter the string : ")
	for s in str :
		if s=="a" or s=="A" :
			vowels["a"]+=1
		elif s=="e" or s=="E" :
			vowels["e"]+=1
		elif s=="i" or s=="I" :
			vowels["i"]+=1
		elif s=="o" or s=="O" :
			vowels["o"]+=1
		elif s=="u" or s=="U" :
			vowels["u"]+=1
	print(vowels)
	print(len(str))
	print("Total number of vowels = ", vowels["a"]+vowels["e"]+vowels["i"]+vowels["o"]+vowels["u"])
	c=input("\nContinue ? (y/n) : ")