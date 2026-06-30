with open ("Sample.txt", "r") as file:
    print(file.read(5))
    print(file.tell())
    print(file.read(20))

with open ("Sample.txt", "r") as file:
    line = file.readline()
    print(line)

#Printing line by line in order
with open("Sample.txt", "r") as file:
    file.readline()# 1 line
    file.readline()# 2 line
    file.readline()# 3 line

with open ("Sample.txt", "r") as file:
    multilines = file.readlines()
    print(multilines)

#Loops with spaces
with open("Sample.txt", "r") as file:
    for i in file:
        print(i)

#Loops with no spaces
with open("Sample.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())

with open("Sample.txt", "r") as file:
    print("Reading only the first 10 characters in file")
    print(file.read(10))

with open("Sample.txt", "r") as file:
    print("Only reading the first line")
    print(file.readline())

with open("Sample.txt", "r") as file:
    print("Reading all the lines")
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("Sample.txt", "r") as file:
    print("Printing all the lines in an array")
    print(file.readlines())

with open("Sample.txt", "r") as file:
    print("printing Through loop")
    for line in file:
        print(line.strip())

with open("Sample.txt", "r") as file:
    text = file.read()
    print(text)

with open("Sample.txt", "r") as file:
    print(file.read(5))

with open("Sample.txt", "a") as file:
    file.write("\nThis line was added")
    
with open("Sample.txt", "r") as file:
    text = file.read()
    print(text)

with open("Sample.txt", "r")as file:
    text = file.read()
    print(text)

with open("Sample.txt", "w") as file:
    file.write("This line will overwrite the entire code")

with open("Sample.txt", "a") as file:
    file.write("\nThis line of code was added at last")