# programe for Binory search
def bsearch(l,n,val):
	found=0
	low=0
	high=n-1
	while low<=high and not (found):
		mid=int((low+high)/2)
		if l[mid]==val:
			found=1
		elif val<l[mid]:
			high=mid-1
		else :
			low=mid+1
	if found :
		return mid
	else :
		return -1
l=[ ]
n=int(input("Enter the number of values : "))
print("Enter the values ")
for i in range(0,n):
	a=int(input(" : "))
	l.append(a)
c='y'
while c=='y' or c=='Y':
	val =int(input("Enter the value to be searched : "))
	p=bsearch(l,n,val)
	if p==-1:
		print("Value not present ")
	else :
		print("Value is present at Position",p+1)
	c=input("\nDo you want to continue ? Y/N : ")
#programe to print maximum value by binoary function
def Findmax(lst,n):
	m= lst[ 0 ]
	low=0
	high=n-1
	for i in range (1,n):
		mid=int((low+high)/2)
		if lst[mid]>m:
			m=lst[mid]
	return m
lst=[ ]
n=int(input("Enter the number of values : "))
print("Enter the values ")
for i in range(0,n):
	a=int(input(" : "))
	lst.append(a)
p=Findmax(lst,n)
print("\nMaximum value is : ",p)