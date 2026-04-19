#create file
f=open("suhani.txt","w")
f.write("my name is suhani\n")
f.close()

#read file
f=open("suhani.txt")
print(f.read())
f.close()

#append file
f=open("suhani.txt","a")
f.write("i live in pune")
print("content appended successfully")
f=open("suhani.txt")
print(f.read())
f.close()


