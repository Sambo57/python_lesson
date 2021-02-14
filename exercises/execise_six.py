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

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry","kiwi", "mango"]
# newlist = ['hello' for x in fruits]
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)


############33 Sort List Alphanumerically ###########33

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 32,656,232]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 22, 434,]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#     return abs(n-50)

# thislist = [100, 50, 65, 76, 17]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "chery"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)


##########3 Copy List ###########


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

############ Join Lists #############

# list1 = ["a", "b", "c"]
# list2 = [4,6,8,]
# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 6]

# for x in list2:
#     list1.append(x)

# print(list1)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 5]
# list1.extend(list2)
# print(list1)

################ List Methods ###############3
#############################################


############ List append ############33

# fruits = [ "apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)

# a = ["apple", "banana", "cherry"]
# b = ["Ford", "BMW", "Volvo"]
# a.append(b)
# print(a)

############ List clear ################3

# fruits = ["apple", "banana", "cherry", "orange"]
# fruits.clear()
# print(fruits)

########## List copy() #############3

# fruits = ["apple", "banana", "cherry", "orange"]
# x = fruits.copy()
# print(x)

############# List count ##########

# fruits = ["apple", "banana", "cherry", "cherry"]
# x = fruits.count("cherry")
# print(x)

# fruits = [1, 3, 34, 545, 45, 455, 45, 454, 45,]
# x = fruits.count(45)
# print(x)

############ List extent() ###########3

# fruits = ["apple", "banana", "cherry"]
# cars = ["Ford", "BMW", "Mers"]
# fruits.extend(cars)
# print(fruits)

# fruits = [ "apple", "banana", "cherry"]
# points = (1, 4 ,6, 7,4)
# fruits.extend(points)
# print(fruits)

#############3 List index() ###########33

# fruits = ["apple", "banana", "cherry"]
# x = fruits.index("banana")
# print(x)

# fruits = [4, 56, 343, 355, 34]
# x = fruits.index(355)
# print(x)

########### List insert() #############33

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(0, "orange")
# print(fruits)


############3 List pop() #############

# fruits = ["apple", "banana", "pineapple"]
# fruits.pop(2)
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# x = fruits.pop(2)
# print(x)


############ List remove() #########

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("apple")
# print(fruits)


############## List reverse() #########3333

# fruits = [ "apple", "banana", "mango"]
# fruits.reverse()
# print(fruits)

############3 List sort() #############

# cars = ["Ford", "BMW", "Kamaz"]
# cars.sort()
# print(cars)

# cars = ["Ford", "BMW", "Volvo"]
# cars.sort(reverse=True)
# print(cars)

# def myFunction(e):
#     return len(e)

# cars = ["Ford","Miysubishi", "BMW", "VW"]
# cars.sort(key=myFunction)
# print(cars)

# def myFunc(e):
#     return e["year"]

# cars = [
#     {"car": "Ford", "year": 2005},
#     {"car": "Mitshubishi", "year": 2000},
#     {"car": "BMW", "year": 2019},
#     {"cae": "VW" , "year": 2011}
# ]
# cars.sort(key=myFunc)
# print(cars)

def myFunc(e):
    return len(e)

cars = ["Ford", "Mitsubishi", "BMW", "VW"]
cars.sort(reverse=True, key=myFunc)
print(cars)