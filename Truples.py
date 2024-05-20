#Progreame to using  tuples 
t1 =(1,2,5,7,9,2,4,6,8,10,11)
#a
n=int(len(t1)/2)
print(t1 [0:n])
print(t1[n: ])
#b
t2 = ("Even values : ")
for i in range(0,len(t1)):
	if t1 [i] % 2 == 0 :
		t2+=str(t1[i])
print(t2)
#c
t2 = (11,13,15)
t1+=t2
print(t1)
#d
print(max(t1))
print(min(t1))
#Input values forom user in a tuple 
vals=input("Enter values , each separated by comma : ")
list=vals.split(" , ")
print(type(list))
tuple = tuple(list)
print("List : " ,list)
print("Tuple  : " ,tuple)

tup = (1,2,3,4)
print(tup)
tup2 = ('a','b')
print(tup2)
#programe to print list
l=[ ]
n=int(input("Enter number of values : "))
for i in range(0,n):
	j=int(input(" : "))
	l.append(j)
print(l)
tuple=tuple(l)
print(tuple)
for i in range(0,n):
 	print(tuple[i])