####################################################
##############   Python Functions
####################################################

# def clear(iterable):
#     iterable.clear()


# numbers = [1, 2, 3, 4]
# clear(numbers)
# print(numbers)

# def fullName(firstName, lastName):
#     return firstName + ' ' + lastName

# print(fullName('Alisher',  'Abdumajidov'))
# print(fullName('Jovohir', 'Davlatov'))

# recentArticles = [
#     {
#         'id': 15,
#         'title': 'This is article 5',
#         'desc': 'This is a decription 5',
#         'author': 'Jamoliddin Yusupov'
#     },
#     {
#         'id': 14,
#         'title': 'This isa article 10',
#         'desc': 'This is a decription 10',
#         'author': 'Jamshid Egamberdiyev'
#     }
# ]

# result = []
# for item in recentArticles:
#     item.pop('id')
#     item.pop('author')
#     result.append(item)
# print(result)


#     {
#         'id': 12,
#         'title': 'This is a article 1',
#         'desc': 'This is a decription 1',
#         'author': 'Farkhod Allamuradov'
#     },
#     {
#         'id': 11,
#         'title': 'This is a article 2',
#         'desc': 'This is a decription 2',
#         'author': 'Sirojiddin Anorqulov'
#     },
#     {
#         'id': 13,
#         'title': 'This is a article 3',
#         'desc': 'This is a decription 3',
#         'author': 'Sirojiddin Bekmurodov'
#     }
# ]

# result = []
# for item in articles:
#     item.pop('id')
#     item.pop('author')
#     result.append(item)

# print(result)


# def removeItems(data = [], items = []):
#     result = []
#     for dataItem in data:
#         for item in items:
#             dataItem.pop(item)
#         result.append(dataItem)
#     return result

# print(removeItems(articles, ['id', 'author']))
# print(removeItems(recentArticles, ['id', 'author', 'desc']))
# print(removeItems())





####################################################
##############   Python Lambda
##################################################

x = lambda a : a + 10
print(x(4))

x = lambda a, b : a * b
print(x(5,6))

def myfunc(n):
    return lambda a : a * n

print(myfunc(5))

doubler = myfunc(5)
print(doubler(7))