# Q.6 The following program is nearly identical to that of the previous exercise. However, this time, it should create a shallow copy of dict1. Be careful: 
# you're not allowed to use the copy module in this exercise.` In addition, before you run this code, can you predict the output values?

dict1 = {
    'a': [{7, 1}, ['aaa', 'aaa']],
    'b': ({3,2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) 

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

# Prediction: These will output as True

# Since a shallow copy is a duplicate of the original object outermost(topmost) level,
# Any nested objects within the copied object are not duplicated. They still 
# reference the nested objects from the original object. dict1 and dict2 are
#different objects and this is why we get a False at the first print.


