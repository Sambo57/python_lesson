
####################################################
##############   Recursion
####################################################

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1) 
#         print(result)
#     else:
#         result = 0
#     return result

# tri_recursion(6)

# k => 0 : result => 0
# k => 1 : result => 1
# k => 2 : result => 3
# k => 3 : result => 6
# k => 4 : result => 10
# k => 5 : result => 15
# k => 6 : result => 21

# def digitRange(digit):
#     if digit > 0:
#         result = digit
#         digit -= 1
#         print(result)
#         digitRange(digit)

# digitRange(9)

# def listSumRecursive(inputList = []):
#     if inputList == []:
#         return 0
#     else:
#         head = inputList[0]
#         smallerList = inputList[1:]
#         return head + listSumRecursive(smallerList)

# print(listSumRecursive([2, 4, 5, 6]))