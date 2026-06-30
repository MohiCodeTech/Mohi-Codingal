# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
def checkifsame(num1, num2):
    if ((num1 ^ num2)!= 0):
        print("They are different numbers")
    else:
        print("They are same numbers")

# checkifsame(num1, num2)

#oddocurring numbers
def OddOccuringNumbers(arr):
    res = 0
    for element in arr:
        res = res ^ element 
    return res

arr = []
n = int(input("Enter the array size: "))
while(n):
    num = int(input("Enter the digit of the array: "))
    arr.append(num)
    n-=1


print("oddoccuring number is ", OddOccuringNumbers(arr))
