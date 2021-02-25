####################################################
##############   Strings 
####################################################


#######   String are Arrays   #######

# arr = ["H", "e", "l", "l", "o"]
# s = "Hello"

# print(arr[2])
# print(s[2])


#######   Looping through a string   #######

# a = "Apple is so juicy fruit!"

# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(a[3])
# # print(a[4])

# for item in a:
#     print(item)


#######   String length   #######

# a = "Apple"

# print(len(a))

# posts = ["Title one", "Title two", "Title three", "Title four"]
# posts = []

# if len(posts) > 0:
#     print("There are {} posts".format(len(posts)))
#     for post in posts:
#         print(post)
# else:
#     print("There is no posts yet!")


#######   Check string   #######

# text = "Bugun havo juda yomon"

# print("juda" in text)

# posts = ["Ob-havo juda yaxshi", "Ob-havo haqida ma'lumotlar", "Xavf yaqinlashmoqda"]
# query = "Ob-havo"

# for post in posts:
#     if query in post:
#         print(post)


####################################################
##############   Slicing strings 
####################################################


#######   Slicing   #######

# a = "Bugun kompyuterim sekin ishlayapti"

# print(a[6:23])
# print(a[:23])
# print(a[6:])
# print(a[-10:-7])
# print(a[-1])


####################################################
##############   Modifiying strings 
####################################################


#######   Uppercase   #######

# a = "Internet juda sekin"
# b = "APPLE"
# c = "   Farhod      "
# d = "Farhod keldi"
# e = "Bizda olma xurmo va olcha bor"

# print(a.upper())
# print(b.lower())
# print(c.strip())
# print(d.replace("Farhod", "Sirijiddin"))
# print(e.split(" "))



####################################################
##############   String Concatenation 
####################################################

#######   String Concatenation   #######


# a = "Salom"
# b = "Bekzod"
# c = a + " " + b

# print(c)



####################################################
##############   String format 
####################################################


# a = 23
# e = 5
# b = "Mening yoshim {1} da, lekin men endi {0} gacha sanashni o'rgandim"
# c = b.format(a, e)

# print(c)



####################################################
##############   Escape Characters
####################################################

# a = "Bu gapda \"kuchli\" mantiq bor"
# b = 'Bu gapda ma\'no yo\'q'
# c = "Bu slash \\ belgisi"
# d = "Qator 1 \nyangi qator"
# e = "Qator 1 \rqator boshi"
# f = "Bu yerda\ttab bor"
# g = "Bu yerda  \btab bor"

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)