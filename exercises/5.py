#########   Python String capitalize() Medhod

# stt = "hello, and welcome to my world."
# x = stt.capitalize()
# print(x)     ## bosh harfini katta harf qilib beradi "CAPITALIZE"

########## String casefold() ############


# ttz = "HELLO, AND WELCOME TO MY WORLD!"
# f = ttz.casefold()
# print(f)         ### Kichkina harf qilib beradi !!!!CASEGOLD!!!!


####### STring center() ######

# ref = "banana"
# d = ref.center(55)
# print(d)           #### Joy tashab ketadi center(55)!


##### String count() ##########

# ere = "I love apples, apple are my fovorite fruit apple"

# x = ere.count("apple")
# print(x) # Stringning ichida nechta bir xil so'zligini sanab beradi!!


##########     String encode()  ##############

# yty = "My name is Sirojiddin"
# x = yty.encode()
# print(x) kodlaydi



######### endswith() ###########

# tyt = "Hello, welcome to my world!"
# x = tyt.endswith("!")
# print(x) ## Nuqta yoki vergul yoki undov beldisi bilan tugaganini bilib beradi endswith.



########### String expandtabs() ###########

# xyx = "H\te\tl\tl\to"

# x = xyx.expandtabs(14)
# print(x)  ### String ichida xoxlagancha harflarning orasida joy tashlash mumkin



########### String find #########

# rer = "Hello, welcome to my world."
# x = rer.find("welcome")
# print(x)



########### String format #########


# ere = "For only {price:.2f} dollars"
# print(ere.format(price = 49))


# txt1 = "My name is {fname}, I'm {age}".format(fname = "Sirojiddin", age = 27)
# txt2 = "My name is {0}, I'm {1}".format("Muslim",6)
# txt3 = "My name is {}, I'm {}".format("Muhammad",1)

# print(txt1)
# print(txt2)
# print(txt3)

######### String index ###########

# txt = "Hello, welcome to my world."
# x = txt.index("welcome")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.index("t")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.index("e", 9, 15)
# print(x)

######### String  isalnum() ##########3

# txt = "Company12"
# x = txt.isalnum()
# print(x)

######### String  isalpha() ##########

# txt = "CompanyX"
# x = txt.isalpha()
# print(x)


######### String  isdecimal() ##########

# txt = "\u0047" #unicode for 3
# x = txt.isdecimal()
# print(x)


######### String  isdigit() ##########

# txt = "50800"
# x = txt.isdigit()
# print(x)

# a = "\u0030"
# b = "\u00B2"

# print(a.isdigit())
# print(b.isdigit())

############ String isidentifier() #########3

# txt = "Demo"
# x = txt.isidentifier()
# print(x)

# a = "MyFolder"
# b = "Demo003"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

############ String islower() #########33

# txt = "hello world!"
# x = txt.islower()
# print(x)

# a = "Hello world!"
# b = "hello 234"
# c = "mynameisPeter"

# print(a.islower())
# print(b.islower())
# print(c.islower())


############ String isnumeric() ############33

# txt = "544444"
# x = txt.isnumeric()
# print(x)
# txt

# a = "\u0030" #unicode for 0
# b = "\u00B2" #unocode for
# c = "10km2"
# d = "-1"
# e = "1.5"

# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())

########## String isprintable() ##########3

# txt = "Hello! Are you #?"
# x = txt.isprintable()
# print(x)

# txt = "Hello!\nAre you #1?"
# x = txt.isprintable()
# print(x)


############ String isspace() ###########

# txt = "  "
# x = txt.isspace()
# print(x)

# txt = "   S   "
# x = txt.isspace()
# print(x)


########## String istitle #############33 

# tx't = "Hello, And Welcome To My World!"
# x = txt.istitle()
# print(x)

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d =  "This Is %'!?"

# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

########### String isupper ##########33

# txt = "THIS IS NOW!"
# x = txt.isupper()
# print(x)

# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS MUSLIM"

# print(a.isupper())
# print(b.isupper())
# print(c.isupper())


########### String join() ########3

# myTuple = ("Jonh", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)

######## String ljust() ###########

# txt = "banana"
# x = txt.ljust(10)
# print(x, "is my favorite fruit.")

# txt = "banana"
# x = txt.ljust(15, "5")
# print(x)

########## String lower() ##########

# txt = "Hello my FRIENDS"
# x = txt.lower()
# print(x)

########33 String lstrip() #######33333

# txt = "       banana           "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite")

# txt = ",,,,,ssaaww.....banana"
# x = txt.lstrip(",.asw")
# print(x)

########### String  maketrans() #########33

# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "R")
# print(txt.translate(mytable))

# txt = "Hi Sam!"

# x = "mSa"
# d = "eJo"
# mytable = txt.maketrans(x, d)
# print(txt.translate(mytable))

######### String partition() #######3333

# txt = "I could eat bananasall day"
# x = txt.partition("bananas")
# print(x)

# txt = "I could eat bananas all day"
# x = txt.partition("apples")
# print(x)

############# String replace() ########333

# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

# txt = "one one was a race horse, two two was one too"
# x = txt.replace("one", "three")
# print(x)

# txt = "one one was a race horse, two two was one too."
# x = txt.replace("one", "three", 1)
# print(x)

########### String rfind() ##########33

# txt = "Mi casa, su casa"
# x = txt.rfind("casa")
# print(x)

# txt = " Hello, welcome to my world."
# x = txt.rfind("e")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.rfind("e", 5, 10)
# print(x)

# txt = "Hello, welcome to my world."
# print(txt.rfind("q"))
# print(txt.rindex("q"))

########### String rindex() #########3

# txt = "Mi casa, su casa"
# x = txt.rindex("casa")
# print(x)

######## String rjust() ##########

# txt = "banana"
# x = txt.rjust(20)
# print(x, "is my favorite fruit")

# txt = "banana"
# x = txt.rjust(20, 0)
# print(x)

########## String rpartition() #########33

# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("bananas")
# print(x)

# txt = "I could eat bananas all day, bananas are my favorite fruit"
# x = txt.rpartition("apples")
# print(x)

######## String rsplit() ##########

# txt = "apple, banana, cherry"
# x = txt.rsplit(",")
# print(x)

# txt = "apple, banana, cherry"
# x = txt.rsplit(",", 1)
# print(x)

####### String split() ############3

# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# txt = "hello, my name is Peter, I am 27  years old"
# x = txt.split(",   ")
# print(x)

# txt = "apple#banana#cherry#orange"
# x = txt.split("#")
# print(x)

# txt = "apple#banana#cherry#orange"
# x = txt.split("#",1)
# print(x)


########### String splitlines() ###########333

# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines()
# print(x)

# txt = "Thank you for the music\nWelcome to the jungle"
# x = txt.splitlines(True)
# print(x)


########## String startswith() ##############

# txt = "Hello, welcome to my world."
# x = txt.startswith("Hello")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.startswith("wel", 7, 20)
# print(x)

#########3 String strip() #############

# txt = "            banana          "
# x = txt.strip()
# print("of all fruits", x, "is my favorite")

# txt = ",,,,,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)

##########3 String swapcase() ##########33

# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

########3 String title() ########3333

# txt = "Welcome to my world"
# x = txt.title()
# print(x)

# txt = "Welcome to my 2nd world"
# x = txt.title()
# print(x)

# txt = "hello b2b2b2 and 3g3g3g"
# x = txt.title()
# print(x)

############## String translate() ##########3

# mydict = {67: 40}
# txt = "Hello Sam!"
# print(txt.translate(mydict))

# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "P")
# print(txt.translate(mytable))

# txt = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = txt.maketrans(x, y)
# print(txt.translate(mytable))

# txt = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = txt.maketrans(x, y, z)
# print(txt.translate(mytable))

# txt = "Goog night Sam!"
# mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
# print(txt.translate(mydict))


###########33 String upper() ###########3

# txt = "Hello my Friends"
# x = txt.upper()
# print(x)


############## String zfill() ###########3

# txt = "50"
# x = txt.zfill(5)
# print(x)

# a = "hello"
# b = "welcome to the jungle"
# c = "10.000"

# print(a.zfill(10))
# print(b.zfill(10))
# print(c.zfill(10))