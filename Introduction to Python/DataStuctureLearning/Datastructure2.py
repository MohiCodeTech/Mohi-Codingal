vegetables = ("Tomato", "potato", "stringbean", "eggplant", "potato")
print("\nPrinting A fruit by accessing its index", vegetables[2])

print("\naccessing last fruit by using negative index", vegetables[-1])

#slicing a tuple
print("\nslicing of tuple 'vegetable' only for tomato and potato ", vegetables[0:2])

print("\nHow much times a specific element is present within the tuple ", vegetables.count("potato"))

print("\nfinding the index within an element ", vegetables.index("Tomato"))

for i in vegetables:
    print(i)

#sets
subjects = {"Maths", "english", "science", "Tamil", "sinhala"}
#add
subjects.add("history")
print(subjects)
#remove
subjects.remove("Maths")
print(subjects)

#number sets
numbers = {1, 2, 3, 4, 5, 6}
numbers.add(7)
print(numbers)
#remove
numbers.remove(1)
print(numbers)

# Union and intersection and difference
set1 = {4, 8 ,9}
set2 = {1, 4, 3}
print("\nunion of both sets ", set1.union(set2))

print("\nintersection of both sets", set1.intersection(set2))

print("\nthe difference of both sets are ", set1.difference(set2))