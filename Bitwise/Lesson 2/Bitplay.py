# def numberofbits(n):
#     ones = 0
#     zeroes = 0
#     while (n):
#         if (n & 1 == 1):
#             ones +=1
#         else:
#             zeroes +=1
#         n >>= 1
#     print("Number of ones are= ", ones, "Number of zeroes are= ", zeroes)
# number = int(input("Enter any number: "))
# numberofbits(number)

def setornoset(n, number):
    if number & (1 << (n - 1)):
        print("SET")
    else:
        print("Not SET")
number = int(input("Enter any number: "))
n = int(input("Enter the bit location: "))
setornoset(n, number)