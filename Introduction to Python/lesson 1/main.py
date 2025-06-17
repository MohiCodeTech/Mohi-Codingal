#This is a main notebook of all lessons if there is a extra file it is for extra activities
# Concantention
str1 = "Hello"
str2 = "World"
combined = str1 + "" + str2
print("The concatened string is, ", combined)

#Repetition
repeated = str1 * 3
print("This is the repeated string ", repeated)

#slicing
slice_str = combined[0:5]
print("This should only print Hello, ", slice_str)

#methods
upper_str = str1.upper()
print("This should only print all UPPERCASE ", upper_str)

lower_str = str2.lower()
print("This should only print all lowercase ", lower_str)

#string length
print("Length of combined string", len(combined))

#Data types
#Integer
num1 = 10
#float
num2 = 20.3
#string
greet = "Good Morning!"
#object
student1 = {
    "name" : "Moheathraam",
    "age" : "14",
    "skills" : "web devolopment"
}
print(student1)
#list (Array)
fruits = ["Apple", "Banana", "orange", "Pinnaple", "grapes"]
#boolean
all_num_are_infinite = True

#Type Casting
string = "hello"
num_contained_str = "200"
boolean = False
Integer = 13
Float = 1.4

#String to int
strtoint = int(num_contained_str)
print("This is type casted conversion of string to integer ", strtoint)

#Int to float
inttofloat = float(Integer)
print("this is integer to float ", inttofloat)

# There are 3 types of loops
#Nested loop, While loop, for loop
#For loops are written like this
for i in range(1,11):
    print("Hello")#What it should do in a loop

#While loop
count = 1
while count <= 5:
       print(count)
       count += 1

#basically nested loop works like a grid for i = 
#nested loop
for i in range(1,4):
       for j in range(1,4):
              print("*", end="")
       print("")

#Turtle Library
#Similarly to other libraries such as time, sys turtle its more artisitic sided