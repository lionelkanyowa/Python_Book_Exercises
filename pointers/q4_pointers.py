# Q.4 Without running this code, what will it print and why?

dict1 = {
    'a': [1, 2, 3, ],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
# print(dict2['a'])

print(id(dict1))
print(id(dict1))
print(dict1 == dict2)
print(dict1 is dict2)

# This will output [1, 42, 3].
# The dict2 is a shallow copy if dict1. The objects are equal but not the same.
# Since dict1 and dict2 contain values with immutable objects, this means that whatever changes made to one dict
# will be reflected to the other dict.
