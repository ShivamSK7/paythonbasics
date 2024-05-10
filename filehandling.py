#programe for looking through a file 
f=open("Text.txt","w")
f.write("This is a cute cat ")
f.write("\nHow are you boy ")
f.close()
#
f=open("Text.txt","r")
for x in f:
	print("*",x)
#
str=input("Enter a string : ")
f=open("Text.txt","r")
for x in f:
	str +=x
	print("*",x)
print("str\n",str)
f.close()
#
f=open("Text.txt","a")
print(f.write("That is a big suprise\nKeep going  "))
f.close()
#
f=open("Text.txt","r")
print(f.read())
f.close()
#
f=open("Text.txt","r")
print(f.read(10))