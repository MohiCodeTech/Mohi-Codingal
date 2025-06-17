age = int(input("Enter your Age: "))
if age >= 18:{
    print("You can vote")
}
else:
    print("you cannot vote")

num1 = int(input("Enter fav number: "))
if num1 % 2 == 0: {
    print("Your favourite number is even!")
}
else:
    print("Your favourite number is odd!")

nestednum = int(input("Enter a Number: "))
if nestednum <= 50:
    print("number is less that 50 and is, ")
    if nestednum % 2 == 0:{
        print("even")
    }
    else:
        print("odd")
else:
    print("too big number")

mathmark = int(input("Enter your maths Marks: "))
if mathmark >= 90:{
    print("Grade A Nice")
}
elif mathmark >= 80:{
    print("Grade B Best you could've done")
}
elif mathmark >= 70:{
    print("Grade C okay buddy hit the books!")
}
elif mathmark >= 50:{
    print("Grade D you were this close to getting a fail")
}
else:
    print("Grade F FAILURE")

import datetime
currentdate = datetime.datetime.now()
print("\nThe current date and time is, ", currentdate)

formatteddate = currentdate.strftime("%d/%m/%Y, %H:%M:%S")
print("\nThis is the modified date and time: ", formatteddate)