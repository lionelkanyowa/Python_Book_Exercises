# Q.3 Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

print(id(dict1))
print(id(dict2))


# The constructor call dict(dict1) creates a new dict that contains the same key/value pairs as dict1.
# Thus, dict2 is not the same object as dict1. Given that the values within dict1 and dict2 are immutable,
# (they contain strings and integers) changes made to one the dictionaries won't reflect to the other.
# The change made to dict2 will not have an effect on the object of dict1.
# Therefore, dict1 will output 'The life of Brian'.
