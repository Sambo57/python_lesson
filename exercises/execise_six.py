############## Loop Through a List ##########

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# thislist = ["apple","banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i= i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x)for x in thislist]


#########33 List Comprehension ##########

# mevalar = ["olma", "banan", "gilos", "kiwi", "mango"]
# newlist = []
# for x in mevalar:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if x != "kiwi"]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits]
# print(newlist)

# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# fruits = ["apple", "banana", "cherry","kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)
