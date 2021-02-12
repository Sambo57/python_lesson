
# fruits = ["apple", "banana", "cherry", "blueberry", "strawberry"]

# for a in range(len(fruits)):
#   print(fruits[a])


# fruits = ["apple", "banana", "cherry", "blueberry", "strawberry"]

# i = 0
# while i < len(fruits):
#   print(fruits[i])
#   i += 1


# fruits = ["apple", "banana", "cherry"]
# [print(x) for x in fruits]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newFruits = []

# for x in fruits:
#   if "n" in x:
#     newFruits.append(x)

# print(newFruits)

# newFruits = [x for x in fruits if "n" in x]
# print(newFruits)


# def customSort(number):
#   return abs(50 - number)

# numbers = [100, 50, 65, 82, 23]
# numbers.sort(key = customSort)
# print(numbers)

# [50, 65, 82, 23, 100]
# [65, 82, 23, 50, 100]
# [82, 23, 50, 65, 100]
# [23, 50, 65, 82, 100]
# [23, 50, 65, 82, 100]

# [50, 65, 23, 82, 100]
#  0   15  27  32  50


# fruits = ["apple", "banana", "cherry"]
# newFruits = fruits
# fruits.append("blueberry")
# print(fruits)
# print(newFruits)
# print(newFruits is fruits)


# fruits = ["apple", "banana", "cherry"]
# newFruits = fruits.copy()
# fruits.append("blueberry")
# print(fruits)
# print(newFruits)
# print(newFruits is fruits)

# allGPA = [4.0, 0.5, 2.5, 1.0, 3.5]
# lowGPA = allGPA.copy()

# for gpa in lowGPA:
#   if gpa > 3:
#     lowGPA.remove(gpa)  

# print(allGPA)
# print(lowGPA)
