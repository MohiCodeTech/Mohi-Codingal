def function1(n):
    return n*(n+1)/2

def function2(n):
    sum = 0
    for i in range(1, n+1):
        sum +1

def function3(n):
    sum = 0
    for i in range(n, n+1):
        for j in range(i, i+1):
            sum +1
            return sum
        
print(function1(5))
print(function2(5))
print(function3(5))