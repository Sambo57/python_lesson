# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(numbers[0])
# print(numbers[2])
# print(numbers[4])
# print(numbers[6])
# print(numbers[8])


# i = 1
# while i < 9:
#     print(i)
#     i += 2

# for i in range(1, 10, 2):
#     print(i)

# for i in range(1,10):
#     if i % 2 == 0:
#         print(i)

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x % 2:
#         count_even += 1
#     else:
#         count_odd += 1
# print("Number of even numbers :", count_even)
# print("Numbers of odd numbers :", count_odd)



# datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'} ]
# for x in datalist:
#     print(type(x))


# numbers = (0, 1, 2, 3, 4, 5, 6)
# for x in numbers:
#     if x == 3:
#         continue
#     print(x)



# for x in range(6):
#     if (x == 3 or x==6):
#         continue
#     print(x,end=' ')
# print("")


# nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Orginal nums list")
# print(nums)
# print("juft nums")
# juft_numbers = list(filter(lambda x : x%2==0, nums))
# print(juft_numbers)
# print("Toq sonlar")
# toq_nums = list(filter(lambda x : x%2 != 0, nums))
# print(toq_nums)


# nl = []
# for x in range(700, 800):
#     if(x %7==0) and (x %5 == 0):
#         nl.append(str(x))
# print(','. join(nl))


# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are""")





# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# nl = []
# for x in range(1566, 3000):
#     if(x %7 ==0) and (x %5 == 0):
#         nl.append(str(x))
# print(','.join(nl))

# import sys
# print(sys.version)        

# import sys
# print("Python version")
# print (sys.version)
# print("Version info.")
# print (sys.version_info)

# import datetime
# m = datetime.datetime.now()
# print(m)


# import math
# class circle():
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * (self.radius**2)
#     def perimeter(self):
#         return 2 * math.pi * self.radius
 
# r = int(input("Введите радиус круга: "))
# obj = circle(r)
# print("Площадь круга:", round(obj.area(), 2))
# print("Длина окружности:", round(obj.perimeter(), 2))

# from math import pi
# r = int(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))



# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
# print("Asli holati")
# print(sonlar)
# print("Juft sonlar")
# juft = list(filter(lambda x : x%2==0, sonlar))
# print(juft)
# print("Toq sonlar")
# toq = list(filter(lambda x : x%2 !=0, sonlar))
# print(toq)



# nl = []
# for x in range(1500, 3000):
#     if(x%7==0) and(x%5==0):
#         nl.append(str(x))
# print(','.join(nl))


# import sys
# print(sys.version)

# import datetime
# now = datetime.datetime.now()
# print(now)

# from math import pi
# r = float(input("radiusni kiriting: "))
# print("The area of the circle with radius" + str (r) + "is" + str (pi * r **2))

# fname = input("Familiyangizni kiriting: ")
# iname = input("Ismingizni kiriting: ")
# print("Assalamu alaykum " + fname + " " + iname)


# nameUser = input("Ismingizni kiriting: ")
# cityUser = input("Shahringizning kiring: ")
# print("Sizning ismingiz {0}. Sizning Shahringizning {1}.".format(nameUser, cityUser))

# res = input("Nechta apelsinni bor? ")
# rrrf = input("Bitta apelsinni narxi qancha? ")



################### 5 ###################

# res = int(res)
# rrrf = float(rrrf)
# sum = res * rrrf           
# print("Narxini to'lang", sum, "so'm")

# fname = input("Input your First Name : ")  
# lname = input("Input your Last Name : ")
# print ("Hello  " + lname + " " + fname) Saytdai javobi!



################### 6 ####################

# user_input = input("ltimos, vergul bilan ajratilgan raqamlar ro'yxatini keltiring, masalan 1, 2, 3, 4: ")
# a_list = list(map(float,user_input.split(',')))
# print(a_list)


# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)                              Saytdagi javob
# print('Tuple : ',tuple)



####################### 8 ###########################

# color_list = ["Red", "Green", "White", "Black"]
# print(color_list[0], color_list[-1])


# list = ["Red","Green","White" ,"Black"]
# print( "%s %s"%(color_list[0],color_list[-1]))  Saytdagi javobi

exam_start_date = (12,10,2018)
print( "The examination will start from : %i / %i / %i"%exam_start_date)




