############################# 1 ####################


# nl = []
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print(','.join(nl))

# nl = []
# for x in range(1400, 1800):
#     if (x%5==0) and (x%4==0):
#         nl.append(str(x))
# print(','.join(nl))


################################# 2 #############################


# temp = input("input the temperature you like to convert? (e.g., 45F, 102C etc.) :")
# degree = int(temp[:-1])
# i_convertion = temp[-1]

# if i_convertion.upper() == "C":
#     result = int(round((9 * degree) / 5 + 32))
#     o_convertion = "Fahrenheit"
# elif i_convertion.upper() == "F":
#     result = int(round((degree -32) * 5 / 9))
#     o_convertion = "Celsius"
# else:
#     print("Input proper convention.")
#     quit()
# print("The temperature in", o_convertion, "is", result, "degrees.")



######################### 3 ########################################


# import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess anumber between 1 and 10 until you get it right : '))
# print('Well guessed!')      ########### Zo'r funksiya ekan!!!!!!!!!!!!!!!


######################## 4 ################################3



# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')


###################### 5 ######################3

# def max_of_two( x, y ):
#     if x > y:
#         return x
#     return y
# def max_of_thee( x, y, z ):
#     return max_of_two( x, max_of_two( y, z ))
# print(max_of_thee(3, 6, -5))


################# 6 ##########################33

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))


################## 7 #####################

# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
# print(multiply((8, 2, 3, -1, 7)))


######################## 8 ##########################


# def string_reverse(str1):

#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))


################ 9 ######################

# r = lambda a : a + 15
# print(r(10))
# r = lambda x, y : x * y
# print(r(12, 4))

# e = lambda b : b + 15
# print(e(50))

# w = lambda d, j : d / j
# print(w(40, 100))

# r = lambda s : s * 90
# print(r(79))

################## 10 ################3



# def func_compute(n):
#     return lambda x : x * n
# result = func_compute(2)
# print("Double the number of 15 =", result(15))
# result = func_compute(3)
# print("Triple the number of 15 =", result(15))
# result = func_compute(4)
# print("Quadruple the number of 15 =", result(15))
# result = func_compute(5)
# print("Quintuple the number 15 =", result(15))



################ 11 ###################3



# subject_marks = [('English', 88), ('Science', 90), ('MAths', 97), ('Social sciences', 82)]
# print("Orginal list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[1])
# print("\nSorting the List of Tuples:")
# print(subject_marks)


################# 12 #######################3


models = [{'make' : 'Nokia', 'model' : 216, 'color' : 'Black'}, {'make' : 'Mi Max', 'model' : '2', 'color' : 'Gold'}, {'make': 'Samsung', 'model': 7, 'color' : 'Blue'}]
print("Orginal list if dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the list of dictionaries :")
print(sorted_models)