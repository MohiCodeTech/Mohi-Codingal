def binary_search(arr, target):
    left, right = 0 , len(arr) -1
    iterations = 0

    while left <= right:
        iterations+=1
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"Found target {target}, in iterations {iterations}")
            return
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid - 1

    print(f"Target {target} not found after iterations {iterations}")

numbers = [1,2,3,4,5,6,7,8,9,10]
# binary_search(numbers, 10)

#Recursion
def count(n):
    if n == 0:
        print("Ended")
        return
    print("The value of count is ", n)
    count(n - 1)

count(10)

#Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

ans = factorial(5)
print("The answer is ",ans )

def create_array(size):
    numbers = []
    for i in range(size):
        numbers.append(i)
    print(numbers)

create_array(10)