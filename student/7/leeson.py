# fruits = [ "apple", "banana", "cherry"]

# for i in range(len(fruits)):
#     print(fruits[i])


# fruits = ["apple", "banana", "cherry", "mango"]
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1 ############ i = i + 1

# fruits = ["apple", "banana", "cherry"]
# [print(x) for x in fruits]


# fruits = ["apple", "banana","cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)

# newlist = [x for x in fruits if "n" in x]
# print(newlist)

# newlist = [x for x in range(10)]
# print(newlist)

# def customSort(n):
#     return abs(n -50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = customSort)
# print(thislist) 

# [50, 65, 83, 23, 100]
# [65, 82, 23, 50, 100]
# [82, 23, 50, 65, 100]
# [23, 50, 65, 82, 100]
# [23, 50, 65, 82, 100]

# [100, 50, 65, 82, 23]
#   50   0  15  32  27

# [50, 65, 23, 82, 100]
#   0  15  27  32  50

# fruits = ["apple", "banana", "cherry"]
# newFruits = fruits
# fruits.append("mango")
# print(fruits)
# print(newFruits)
# print(newFruits is fruits)


# fruits = ["apple", "banana", "cherry"]
# newFruits = fruits.copy()
# fruits.append("mango")
# print(fruits)
# print(newFruits)
# print(newFruits is fruits)

# allGPA = [4.0, 0.5, 2.5, 1.0, 3.5]
# LowGPA = allGPA.copy()

# for gpa in LowGPA:
#     if gpa > 3:
#         LowGPA.remove(gpa)

# print(allGPA)
# print(LowGPA)