# def printnumber(n):
#     iteneration = 0
#     print("The total number entered by the user is", n)
#     iteneration+=1
#     print("total itineration done by computer is", iteneration)

# printnumber(10)
# printnumber(200)

# print("With the number entered by the user doesnt change the time taken by computer")

def ontime(n):
    iteration = 0
    for i in range(1, n+1):
        iteration+=1
    print("When n is", n, "iterations = ", iteration)

ontime(5)
ontime(10)
ontime(2)

print("\nWith every n the time taken and iteration will incease linearly")