name = input("Enter your name!: ")
age = int(input("Enter your age as well!: "))
favfood = input("What is your favourite food?: ")
favcolour = input("And your favourite colour!: ")

def conversation(name, age, favfood, favcolour):
    print(f"Hello {name} welcome to codingal!")
    print(f"You are {age} years old!")
    if age >= 18:
        print("Nice! You can vote now!")
    else:
        print("You are still young! please come back after some years")

    print(f"Your favourite food is {favfood}!")
    if favfood.upper() == "DOSA":
        print("Wow! That is also the favourite food of the creator!")
    else:
        print("Nice Selection!")

    print(f"Your favourite colour is {favcolour}!")

    if favcolour.upper() == "red":
        print("Nice! red is a fantastic colour in my choice")
    else:
        print("It is a amazing colour indeed")
    print("So this is the end of the program bye!")

conversation(name, age, favfood, favcolour)

#recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
ans = factorial(12)
print(f"factorial of {num} is {ans}")