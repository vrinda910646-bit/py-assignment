#file_exception.py
filename=input("enter filename:")

try:
    with open(filename,"r") as file:
        print(file.read())

except FileNotFoundError:
    print("error:file does not exist")

except PermissionError:
    print("error:permission denied")