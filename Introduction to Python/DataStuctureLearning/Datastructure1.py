fruits = ["apple", "banana", "pineapple"]
print(fruits)
print(fruits[0])

#appending
fruits.append("mango")
print("After appending 'mango' the array it looks like this: ", fruits)

#removing
fruits.remove("apple")
print("The version of the array removing apple is: ", fruits)

#intinerating
for x in fruits:
    print(x)

subjects = ["maths", "english", "science", "history"]
subjects.append("IT")
print(subjects)

subjects.remove("history")
print("the marks that i get high is: ", subjects)

for x in subjects:
    print(x)

#Dictionaries
student = {
    "name" : "Moheathraam",
    "age" : 14,
    "grade" : "9th grade"
}

student["school"] = "st.Johns college"
print("this is the  student dictionary printed with the 'school'key, and value", student)

del student["age"]
print(student)



print("intinerating throught 'student'dictionary!")
for key, value in student.items():
    print(key, ":", value)