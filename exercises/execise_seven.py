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

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.update(y)
# print(x)

####################### DICTIONARIES ##################
####################################################3###

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }


# thisdict = {
#      "brand": "Ford",
#      "model": "Mustang",
#      "year": 1964
# }
# print(thisdict)


# thisdict = {
#      "brand": "Ford",
#      "model": "Mustang",
#      "year": 1964
# }
# print(thisdict["brand"])

# thisdict = {
#      "brand": "Ford",
#      "model": "Mustang",
#      "year": 1964,
#      "year": 2020
# }
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "electric": False,
#     "year": 1964,
#     "colors": ["red", "white", "blue"] 
# }
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# print(type(thisdict))

################## Access Dictionary items ##########3

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2020
#     }
# x = thisdict["model"]
# print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2020
#     }
# x = thisdict.get("model")
# print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2020
#     }
# x = thisdict.keys()
# print(x)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.keys()

# print(x)

# car["color"] = "white"

# print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict.values()
# print(x)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.values()

# print(x)

# car["year"] = 2020

# print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = thisdict.items()
# print(x)


# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# x = car.items()

# print(x)

# car["year"] = 2020

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# if "model" in thisdict:
#     print("Yes, 'model' is one of the keys in the thisdict dictionary")

################3Change Dictionary Items ############

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)


################# Adding Items ###############33

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)

############## Remove Dictionary Items ############

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# del thisdict["model"]
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# del thisdict
# print(thisdict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# thisdict.clear()
# print(thisdict)

############## Loop Dictionaries ###############33

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964
# }
# for x in thisdict:
#     print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964
# }
# for x in thisdict:
#     print(thisdict[x])

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964
# }
# for x in thisdict.values():
#     print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964
# }
# for x in thisdict.keys():
#     print(x)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964
# }
# for x, y in thisdict.items():
#     print(x, y)

############## Copy Dictionaries #############

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

############### Nested Dictionaries ############

# myfamily = {
#     "child1" : {
#       "name" : "Muslim",
#       "year" : 2014
#     },
#     "child2" : {
#       "name" : "Soliha",
#       "year" : 2017
#     },
#     "child3" : {
#       "name" : "Muhammad",
#       "year" : 2019
#     }
# }
# print(myfamily)

# child1 = {
#     "name" : "Emil",
#     "year" : 2000
# }
# child2 = {
#     "name" : "Tobias",
#     "year" : 2003
# }
# child3 = {
#     "name" : "Linus",
#     "year" : 2011
# }
# myfamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3
# }
# print(myfamily)

############# Dictionary Methods ################3
#################################################

############## Clear() #########################

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964 
#  }
# car.clear()
# print(car)

################ Copy() ###############33

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964 
#  }
# car.copy()
# print(car)

############# Fromkeys() ###############3

# x = ('key1', 'key2', 'key3')
# y = 0
# thisdict = dict.fromkeys(x, y)
# print(thisdict)

# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x)
# print(thisdict)

############### Get() ###############3

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.get("model")
# print(x)

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.get("price", 15000)
# print(x)

############# Items() ##############

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.items()
# print(x)

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.items()
# car["year"] = 2018
# print(x)

################# Keys() ###############33

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.keys()
# print(x)

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.keys()
# car["color"] = "white"
# print(x)

##############3 Pop() ##############3

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# car.pop("model")
# print(car)

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.pop("model")
# print(x)

############### Popitem() ##############

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# car.popitem()
# print(car)

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.popitem()
# print(x)

###############3 Setdefault() ################

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.setdefault("model", "Bronco")
# print(x)

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# x = car.setdefault("color", "white")
# print(x)

################## Update() ###################3

# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 1964
# }
# car.update({"color": "White"})
# print(car)

############## Values() ############3

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
x = car.values()
print(x)

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}
x = car.values()
car["year"] = 2018
print(x)