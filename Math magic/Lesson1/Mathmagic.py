# #Check if your number is an armstrong number
# number = int(input("Enter an armstrong number: "))
# result = 0
# temp = number
# while temp != 0:
#     digit = temp % 10
#     result = result + digit**3
#     temp = temp//10

# if number == result:
#     print(f"{number} is an armstrong number")
# else:
#     print(number, "is not an armstrong number")

#Factors of numbers
# factor_number = int(input("Enter any number to find its factor: "))

# print(f"Factors of {factor_number} are: ", end="")
# for i in range(1, factor_number +1):
#     if factor_number % i == 0:
#         print(i)

num = int(input("Enter a number to convert it into roman numeral: "))

roman_dic = {
    1: 'I', 4:'IV', 5:'V',9:'IX',10:'X',40:'XL',50:'L',
    90:'XC', 100:'C', 400:'CD',500: 'D', 900: "CM",  1000:'M'
}
result = ""
for value in sorted(roman_dic.keys(), reverse=True):
    while num>= value:
        result += roman_dic[value]
        num -= value
print("Roman numeral is", result)