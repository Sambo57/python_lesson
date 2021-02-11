
####################################################
##############   List #############################
###################################################

# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# #Ordered

# print(fruits[0])
# print(fruits[1])

# Changeable

# fruits[0] = "strawberry"
# print(fruits)

# Allow duplicates

# fruits.append("banana")
# print(fruits)

# print(len(fruits))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 4, 6, 78, 778.7]
# list3 = [True, False, True]

# list4 = ["apple", 23, True, "male", False, 6.8]

# print(type(fruits))

# newlist = list(("apple", "banana", "cherry"))
# print(newlist)

# thislist = ["apple", "banana","cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi","mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list")


########## Change List Items ###########

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

########## Change a Range of Item Values ###########

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist) 

# thislist = ['apple', "banana", "cherry"]
# thislist.insert(3, "watermelon")
# print(thislist)

##########3  Add List Items ############33

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

########### Add Any Iterable ##########3

# thislist = ["apple", "banana", "cherry"]
# thistuple = {"kiwi", "orange"}
# thislist.extend(thistuple)
# print(thislist)

# x = 4*3//2**2
# print(x)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(0)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)


thislist = ["apple", "banana", "cheery"]
thislist.clear()
print(thislist)