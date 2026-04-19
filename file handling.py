#create file
file=open("shruti.txt","w")
f.write("hello shruti\n")
print("file created")

#read file
f=open("shruti.txt")
print(f.read())
f.close()

#append
f=open("shruti.txt","a")
f.write("i was studying")
print("content appended")
f=open("shruti.txt")
print(f.read())
f.close()
