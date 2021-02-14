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
thistuple = (1, 4, 343, 565, 34, 5, 65, 656, 4,  53, 23)
x = thistuple.index(34)
print(x)