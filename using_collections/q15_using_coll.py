# Q.15 without running the following code, what values will be printed by line 10?

pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# Line 10 will print

# (['Cat', 'Bird', 'Snake'])
