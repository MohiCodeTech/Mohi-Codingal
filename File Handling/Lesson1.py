# file = open("Sample.txt", "r")
# text = file.read()
# print(text)
# file.close()

# file = open("Sample.txt", "w")
# file.write("\nChanged hello to whom, \nChanged how to where, \nchanged why to what")
# file.close()

# file = open("Sample.txt", "r")
# text = file.read()
# print(text)
# file.close()

# file = open("Sample.txt", "a")
# file.write("\nWhere, \nWhat")
# file.close()

# file = open("Sample.txt", "r")
# text = file.read()
# print(text)
# file.close()

with open("Sample.txt", "w") as file:
    file.write("\nHow are you doing?")
    file.write("\nWhats with them?")

with open("Sample.txt", "r") as file:
    text = file.read()
    print(text)

with open("Sample.txt", "a") as file:
    file.write("\nGOOD")
    file.write("\nBAD")

with open("Sample.txt", "r") as file:
    text = file.read()
    print(text)
