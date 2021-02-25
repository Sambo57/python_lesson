########################################
################ Dictanary Items - DAta Types
##########################################

# myDict = {
#     "brand" : "Ford",
#     "electric" : False,
#     "year" : 1964,
#     "colors" : ["red", "white", "blue"]
# }
# # print(myDict["colors"][0])

# product = {
#     "id": 23,
#     "name": "T-shirt",

#     "colors": [
#         {
#         "id": 1,
#     "name": "red"
#         },
#     {
#         "id": 3,
#         "name": "blue"
#     },
#     {
#         "id": 11,
#         "name": "orange"
#     },
# ]
# }

# output = "Name: " + product["name"] + ", Colors: "
# for color in product["colors"]:
#     output += color["name"]
#     if color["id"] != product["colors"][-1]["id"]:
#         output += ","
# print(output)


###################3###########################
############## Loop Through a Dictionary#########
##################################################

# myCar = {
#     "name" : "Mustang",
#     "color": "Black",
#     "year" : 2007
# }

# for key in myCar:
#     print(key)
# for key in myCar:
#     print(myCar[key])

# for value in myCar.values():
#     print(value)


# for key, value in myCar.items():
#     print(key, value)


#######################################
################# Nested Dictionaries
#####################################

# myfamily = {
#     "wife": {
#         "name" : "Jane",
#         "year" : 1995
#     },
#     "daughter" : {
#         "name" : "Sarah",
#         "year" : 2014
#     }
# }

# print(myfamily["daughter"]["name"])

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

x = car.setdefault("model", "Bronco")
print(x)