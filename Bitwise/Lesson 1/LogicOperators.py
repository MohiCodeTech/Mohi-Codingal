# num1 = 10
# num2 = 4
# print("num1 & num2 are :", num1 & num2)
# print("num1 | num2 are :", num1 | num2)
# print("num1 ^ num2 are :", num1 ^ num2)
# print("num1 >> num2 are :", num1 >> num2)
# print("num1 << num2 are :", num1 << num2)
# print("~num1 are",~num1)
# print("~num2 are", ~num2)


#Logics
# def isEvenOdd(n):
#     if(n ^ 1 == n + 1 ):
#         return True
#     else:
#         return False

# number = int(input("Enter any number: "))
# if isEvenOdd(number):
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

#Number of bits
def numberofBits(n):
    count = 0
    while(n):
        count +=1
        n >>= 1
    return count

n = int(input("Enter any number: "))
print("Number of bits is: ",numberofBits(n))