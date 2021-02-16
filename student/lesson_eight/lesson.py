
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple", "banana"}

# z = x.difference(y) 
# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple", "banana"}

# x.difference_update(y) 
# print(x)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
w =y.issuperset(x)

print(w)
print(z)