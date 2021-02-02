####################################################
##############   Strings 
##########################################

#######   String are Arrays   #######

# fer = ["H","e", "l", "l", "o"]
#s = "Hello"

# print(fer[4])
# print(s[1])

#######   String are Arrays   #######

# a = "Olma juda mazzali ekan!"

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# for it in a:
#   print(it)


#######   String length   #######

#a = "Pineapple"
#print(len(a))

# posts = ["Title one","Title two", "Title three"]


# if len(posts) > 0:
#    print("There are {} posts".format(len(posts)))
#    for post in posts:
#        print(post)
#else:
#    print("There is no posts yet!")   
     

#######   Check string   #######

# text = "Bugun havo juda yomon"

# print("juda" in text)

# posts = ["Ob-havo juda yaxshi", "Ob-havo haqida ma'lumotlar", "Xavf yaqinlashmoqda"]
# query = "Ob-havo"

# for post in posts:
  #  if query in post:
   #    print(post)

# txt = "The best things in life are free!"
# if "free" in txt:
#  print("Yes, 'free' is present.")

#######   Slicing   #######

# a = "Bugun kompyuterim sekin ishlayapti"

# print(a[5:23])
# print(a[:35])
# print(a[-10:-7])
# print(a[-1])

####################################################
##############   Modifiying strings 
####################################################

######### Uppercase #########

# a = "Internet juda sekin "
# b = "APPLE"
# c = "     Javohir     "
# w = "Muslim keldi"
# l = "Bizda Xumo banan va nok bor"

# print(a.upper())
# print(b.lower())
# print(c.strip())
# print(w.replace("Muslim","Jasur"))
# print(l.split("  "))

####################################################
##############   String Concatenation 
##################################################

#######   String Concatenation   #######

# a = "Assalamu alaykum"
# b = "Otabek"
# r = a + " " + b
# print(r)

####################################################
##############   String format 
####################################################

# a = 32
# t = "mashina"
# g = "Mening yoshim {} da, lekin men {} xayday olmayman"
# s = g.format(a,t)
# print(s)

####################################################
##############   Escape Characters
###################################################

# s = 'Bu gapda \"kuchli\" mantiq bor'
# d = "Bu gapda ma\'no yo'\q" 
# f = "Bu slash \\ belgisi"
# g = "Qator 1 \nyangi qator"
# h = "Qator 1 \rqator boshi"
# j = "Bu yerda \t tab bor"


# print(s)
# print(d)
# print(f)
# print(g)
# print(h)
# print(j)