for i in range(1,11):
         print(f"Hello : {i}")

# loop on array
fruits = ["apple", "banana", "Pineapple"]
for x in fruits:
    print(x)

vegetables = ["eggplant", "Stringbeans", "Potato", "Spinach"]
for x in vegetables:
       print(x)

#char loop
name = "Python"
for char in name:
       print(char)

actname = "Moheathraam"
for char in actname:
       print(char, end="")

#While loop
count = 0
while count <= 5:
       print(count)
       count += 1

#nested loop
for i in range(1,4):
       for j in range(1,4):
              print("*", end="")
       print("")

#Multiplication table from 1 to 6
for i in range(1,6):
       for j in range(1,6):
              print(f"{i * j}", end="\t")
       print()

for i in range(1,5):
       for j in range(1,3):
              print("*", end="")
       print("")