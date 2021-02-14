############# TUPLES ##############

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# thistuple = tuple(("apple", "banana", "cherry"))
# print(len(thistuple))

# thistuple = ("apple",)
# print(type(thistuple))

# thistuple = ("apple")
# print(type(thistuple))

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 2, 3, 6, 3)
# tuple3 = (True, False, False)

# print(tuple1)
# print(tuple2)
# print(tuple3)

# tuple1 = ("abs", 34, True, 40, "male")
# print(tuple1)

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)


########### Access Tuple Items #############

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:5])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[:4])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[2:])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#     print("Yes, 'apple' is in the fruits tuple")


################## Update Tuples ##################3

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)

# thistuple = ("apple", "banana", "cherry")
# thistuple.append("orange")
# print(thistuple)  # This will raise an error


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)


############3 Unpack Tuples ##########3

# fruits = ("apple", "banana","cherry")
# (x, y, d,) = fruits

# print(x)
# print(y)
# print(d)

###### Using Asterix* #########

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (a, b, *s) = fruits
# print(a)
# print(b)
# print(s)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
# (a, *tropic, b) = fruits
# print(a)
# print(tropic)
# print(b)

######### Loop Tuples ##########

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)

# thistuple = ("apple", "banana", "cherry", "mango", "strawberry")
# for i in range(len(thistuple)):
#     print(thistuple[i])

# thistuple = ("apple", "banana", "cherry", "mango")
# i = 0
# while i < len(thistuple):
#     print(thistuple[i])
#     i = i + 2

######### Join Tuples #######

# tuple1 =("a", "b","c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 3
# print(mytuple)

############# Tuple count() ############33

# thistuple = (1, 2, 3, 4, 5, 7, 45, 5, 343, 5, 8)
# x = thistuple.count(5)
# print(x)


############# Tuple index() ############
# thistuple = (1, 4, 343, 565, 34, 5, 65, 656, 4,  53, 23)
# x = thistuple.index(34)
# print(x)


###################### SET ########################
####################################################

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 10, 5, 88}
# set3 = {True, False, True}

# print(set1)
# print(set2)
# print(set3)

# set1 = {"abs", 34, True, 49, "male"}
# print(set1)

# myset = {"apple", "banana", "cherry"}
# print(type(myset))

# thisset = set(("apple", "banana", "cherry"))
# print(thisset)

############### Access Set Items #############3

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)

# thisset = {"apple", "banana", "cherry"}
# print("apple" in thisset)

############ Add Set Items ################

# thisset = {"apple", "banana", "cherry"}
# thisset.add("mango")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

################## Remove Set Items ###############3

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("apple")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# thisset.discard("cherry")
# print(thisset)

# thisset = {"apple", "banana", "cherry"}

# x = thisset.pop()
# print(x)

# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset 
# print(thisset)

############### Loop Items #############3

# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)

################ Join Two Sets ################

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z) 

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)

############### Set Methods ################
############################################

############ Add() #######################


# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# fruits = {"apple", "banana", "cherry"}
# fruits.add("apple")
# print(fruits)


############### Clear() ###############33

# fruits = {"apple", "banana", "cherry"}
# fruits.clear()
# print(fruits)

############## SET COPY() ####################3

# fruits = {"apple", "banana", "cherry"}
# x = fruits.copy()
# print(x)

############ SET Difference() ##############333

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = y.difference(x)
# print(z)

########### SET Difference_update() ###########33

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y)
# print(x)

############ Set discard() ##########333

# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)

########### Set intersection() ###########333

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# result = x.intersection(y, z)
# print(result)

############# Set intersection_update() ############3

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}
# x.intersection_update(y, z)
# print(x)

############### Set isdisjoint() #############

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "fecebook"}
# z = x.isdisjoint(y)
# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.isdisjoint(y)
# print(z)

############ Set issubset() #############3

# x = {"a", "b", "c"}
# y = {"f", "e", "c", "b", "a"}
# z = x.issubset(y)
# print(z)

# x = {"a", "b", "c"}
# y = {"f", "e", "c", "b"}
# z = x.issubset(y)
# print(z)


############ Set pop() ##############

# fruits = {"apple", "banana", "cherry"}
# fruits.pop()
# print(fruits)

# fruits = {"apple", "banana", "cherry"}
# r = fruits.pop()
# print(r)

#############3 Set remove() ############3

# fruits = {"apple", "banana", "cherry"}
# fruits.remove("cherry")
# print(fruits)

########### Set symric_difference() ##########33

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)


############ Set symric_difference_update() ###########3


# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

########### Set union() #############

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.union(y)
# print(z)

# x = {"a", "b", "c"}
# y = {"f", "d", "a"}
# z = {"c", "d", "e"}
# result = x.union(y, z)
# print(result)

############3 Set update() ###########3

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)