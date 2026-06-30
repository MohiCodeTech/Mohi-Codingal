#Prime number
#example one
# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n+1):
#     if n%i== 0:
#         count +=1

# if count == 2:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")

#example two
# n = int(input("Enter any number which is bigger than 2: "))
# for i in range(2,n):
#     if n%i == 0:
#         print(f"{n} is not a prime number")
#     else:
#         print(f"{n} is a prime number")


#Sieve metod
def Sieve(n):
    primes = [True] * (n+1)
    primes[0]  = primes[1] = False,
    
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1 ,i):
                primes[j] = False
    
    for i in range(n+1):
        if primes[i]:
            print(i, end=" ")

limit = int(input("Enter the limit: "))
Sieve(50)