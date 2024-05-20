# programe to do selection short
def selsort (list, n):
	j=n-1
	while j>0:
		large =list[0]
		index = 0
		for i in range (1,j+1):
			if list[i]> large:
				large=list[i]
				index=1
		list[index]=list[j]
		list[j]=large
		j-=1
list=[ ]
n=int (input ("Enter the number of values "))
print ("Enter the Vlaues ")
for i in range (0, n) :
	a = int (input (": "))
	list.append(a)
selsort (list, n)
print("\nSorted list : \n") 
for i in range (0, n) :
	print (list [i])
# programe to do insertion short
def inshort(list,n):
	for i in range(1,n):
		currentVal=list[i]
		pos=i
		while pos>0 and currentVal<list[pos-1]:
			list[pos]=list[pos-1]
			pos=pos-1
			list[pos]=currentVal
list=[ ]
n=int(input("Enter the number of values : "))
print("Enter the values ")
for i in range(0,n):
	a=int(input(" : "))
	list.append(a)
inshort(list,n)
print("\nShorted list ; \n ")
for i in range(0,n):
	print(list[i])