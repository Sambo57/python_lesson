######################################
###########Functions ################

# def my_function():
#     print("assalamu alaykum")
# my_function()

# def my_function(fname):
#     print(fname + " Husanov")

# my_function("Muslim")
# my_function("Muhammad")

# def my_function(*kids):
#     print("The youngest child is " + kids[1])

# my_function("Muslim", "Muhammad")

# def my_function(child3, child2, child1):
#     print("The yourgest child is " + child3)

# my_function(child1 = "EMil", child2 = "Tobias", child3 = "Linus")

# def my_function(**kid):
#     print("His last name is " + kid["fname"])

# my_function(fname = "Tobias", lname = "Refnes")

# def my_function(mtt = "Germany"):
#     print("I am from " + mtt)
# my_function("Sweden")
# my_function("Uzb")
# my_function()
# my_function("Brazil")

# def my_function(food):
#     for x in food:
#         print(x)
# fruits = [ "apple", "banana", "cherry"]
# my_function(fruits)

# def my_function(x):
#     return 5 * x

# print(my_function(5))
# print(my_function(8))
# print(my_function(19))

# def myfunction():
#     pass

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return  result
# print("\n\nRecursion Example Result")
# tri_recursion(6)


#############################################
################ Lambda #####################

# x= lambda a: a + 10
# print(x(5))

# x = lambda a, b: a * b
# print(x(5, 6))

# x = lambda a, b, c: a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#     return lambda a : a * n
# mydoubler = myfunc(3)
# print(mydoubler(11))\


# def myfunc(n):
#     return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(33))


#######################################
################# Arrays #############

# cars = ["Ford", "Volvo", "BMW"]

# print(cars)

# cars = [ "Ford", "Volvo", "BMW"]
# x = cars[2]
# print(x)

# cars = ["Ford", "Volvo", "BMW"]
# cars[1] = "Tesla"

# print(cars)


# cars = ["Ford", "Tesla", "BMW"]
# x = len(cars)
# print(x)

# cars = ["Ford", "Tesla", "BMW"]
# for x in cars:
#     print(x)

# cars = ["Ford", "Tesla", "BMW"]
# cars.append("Honda")
# print(cars)

# cars = ["Ford", "Tesla", "BMW"]
# cars.pop(0)
# print(cars)

# cars = ["Ford", "Tesla", "BMW"]
# cars.remove("Ford")
# print(cars)

############################################
############### Classes and Objects ########

# class MyClass:
#     x = 0

# print(MyClass)

# class MyClass:
#     x = 7
# danger = MyClass()
# print(danger.x)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print (p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()

# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age

#     def myfunc(abc):
#         print("Hello my name is " + abc.name)

# p1 = Person("John", 34)
# p1.myfunc()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)
    
# p1 = Person("John", 36)
# p1.age = 40
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)

# del p1.age

# print(p1.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def myfunc(self):
#         print("Hello my name is " + self.name)

# p1 = Person("John", 46)

# del p1

# print(p1)

# class Person:
#     pass


nl = []
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print(','.join(nl))

