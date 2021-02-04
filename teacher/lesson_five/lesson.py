####################################################
##############   Booleans 
####################################################


#######   Boolean Values   #######

# print(False)
# print(10 > 0)
# print(10 == 9)
# print(10 > 11)

# a = 200
# b = 33

# if b > a:
#     print("b a dan katta")
# else:
#     print("b a dan katta emas")

# print(bool("Hello"))
# print(bool(15))

# x = "Salom"
# y = 15

# print(bool(x))
# print(bool(y))


#######   Most Values are True   #######

# print(bool("abc"))
# print(bool(134))
# print(bool(["apple", "cherry", "banana"]))


#######   Some Values are False   #######

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# class myClass():
#     def __len__(self):
#         return 0

# myObject = myClass()
# print(bool(myObject))


#######   Functions can Return a Boolean   #######

# def myFunction():
#     return False

# print(myFunction())

# if myFunction():
#     print("YES!")
# else:
#     print("NO!")

# x = 200
# print(isinstance(x, int))


####################################################
##############   Python Operators
####################################################


#######   Python Arithmetic Operators   #######

# 5 ** 3  =  5 * 5 * 5 
# 5 ** 5  =  5 * 5 * 5 * 5 * 5

# print(5**5)

# print(7//2)


#######   Python Assignment Operators   #######

# x = 5
# print(x)
# x = x + 5
# print(x)

# x = 5
# x += 7
# print(x)

# numbers = [0, 3, 45, 12, 567]

# sum = 0
# sum += numbers[0]
# sum += numbers[1]
# sum += numbers[2]
# sum += numbers[3]
# sum += numbers[4]
# print(sum)

# sum = 0
# for number in numbers:
#     sum += number
# print(sum)

# print(True and True)
# print(True and False)
# print(False and False)

# print(True & True)
# print(True & False)
# print(False & False)



#######   Python Identity Operators   #######

# x = 4
# y = x
# z = "Apple"

# print(y is x)
# print(y is not x)
# print(z is x)


#######   Python Membership Operators   #######

# x = "Salom do'stlar"
# y = "Salom"

# print(y in x)

# a = [3, 4, 6, "Hello", 34.6]
# b = 5
# c = 4

# print(b in a)
# print(c in a)
# print(b not in a)