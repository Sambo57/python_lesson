# Variables

# son = 10
# print(son)


# Output variables

# x = "Salom "
# y = "Farhod"
# z = x + y
# print(z)

# x = 10
# y = 15
# print(x + y)

#x = "5"
#y = 5
#print(x + y)

# Global variables

x = "salom"

def myFuncOne():
    print(x + " Farhod")

def myFuncTwo():
    global x
    x = "Hello"
    print(x + " Farhod")


# myFuncOne()
# myFuncTwo()

# print(x)

# Function

# def caculateMedian(numbers):
#     sum = 0
#     for item in numbers:
#         sum += item
#     result = sum / len(numbers)
#     return result

# print(caculateMedian([2, 4, 7, 45, 56, 57, 84, 89, 1001]))
# print(caculateMedian([42, 45, 135]))
# print(caculateMedian([42, 45, 23, 45]))
# print(caculateMedian([42, 135]))
