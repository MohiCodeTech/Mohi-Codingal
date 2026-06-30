with open("Sample.txt", "w") as file:
    file.write("This is a new line")
    file.write("\nAnother line")
print("Data written to text is successful")

text = "App development programming language is python"
with open("Sample.txt", "w") as file:
    words = text.split()
    print(words) #Array form
    for word in words:
        file.write(word + "\n")
print("The new data has overwritten the current data")

with open("Sample.txt", "r") as file:
    read = file.read()
    print(read)

try:
    with open("Hello.txt", "x") as file:
        file.write("This is a newly created file")
    print("file created successfully")
except FileExistsError:
    print("The file already exists")