# def power2(number):
#     if number <= 0:
#         return False
#     else:
#         return (number & (number - 1) == 0)
    
# number = int(input("Enter a number to check if it is a power of 2: "))

# if power2(number):
#     print("The number is a power of 2")
# else:
#     print("The number is not a power of 2")

# #Powerof4
# def power4(number):
#     if number <= 0:
#         return False
#     else:
#         return (number & (number - 1) == 0 and (number - 1) % 3 == 0)
    
# number = int(input("Enter a number to check if it is a power of 4: "))

# if power4(number):
#     print("The number is a power of 4")
# else:
#     print("The number is not a power of 4")

def Compute_Power(x, y):
    result = 1
    while y>0:
        if(y % 2 == 0):
            x = x * x
            y >>= 1
        else:
            result = result * x
            y = y -1
    return result

x = int(input("Input a number: "))
y = int(input("Input another number: "))

print("Total is ", Compute_Power(x, y))