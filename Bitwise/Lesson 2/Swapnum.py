# def swap(a, b):
#     a = a^b
#     b = a^b
#     a = a^b
#     print("The numbers are now swapped a = ", a, "b = ", b)

# def swap2(a,b):
#     a = (a & b) + (a | b)
#     b = a+(~b) + 1
#     a = a+(~b) + 1
#     print("The numbers are now swapped a = ", a, "b = ", b)

# swap(5, 4)
# swap2(10, 20)

#Divide without using the sign
def dividewithoutsign(ourdivident, ourdivisor):
    sign = (-1 if((ourdivident < 0) ^ (ourdivisor < 0)) else 1)
    ourdivident = abs(ourdivident)
    ourdivisor = abs(ourdivisor)

    quotientnumber = 0
    tempnumber = 0
    for i in range (31, -1, -1):
        if( tempnumber + (ourdivisor << i) <= ourdivident):
            tempnumber += ourdivisor << i
            quotientnumber |= 1 << i
        if sign == -1:
            quotientnumber = -quotientnumber
        return quotientnumber

a = int(input("Enter a number to divide a/b: "))
b = int(input("Enter a number to divide a/b: "))
print("result of ", a, "/", b ,"is", dividewithoutsign(a, b))

