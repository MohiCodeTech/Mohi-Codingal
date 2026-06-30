# number = int(input("Please enter a number: "))
# original_num = number
# reverse_num = 0

# while number > 0:
#     digit = number % 10
#     reverse_num = reverse_num * 10 + digit
#     number //= 10

# if original_num == reverse_num:
#     print(f"The number {original_num} is a palindrome number")
# else:
#     print(f"The number {original_num} is not a palindrome number")

#HCF
# large_number = int(input("Enter the largest number: "))
# small_number = int(input("Enter the smallest number: "))

# while small_number:
#     number_store = small_number
#     small_number = large_number % small_number
#     large_number = number_store

# print("HCF is ", large_number)

#LCM
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a>b:
    greater = a
else:
    greater = b

while True:
    if(greater % a == 0) and (greater % b == 0):
        print("LCM is ", greater)
        break
    greater += 1
    