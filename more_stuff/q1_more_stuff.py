# Q.1 What does the following function do? Be sure to Identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Claire':   175,
    'Karin':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# Line 15 invokes the method in line 3.When the method is invoked, it passes through
# the my_dict dictionary as an argument. line 4 returns the keys of a sorted dictionary.
# Chaining is then used to get the sorted dictionary and key index 1.
# The upper method is called at key index 1 which outputs 'CHRIS'

   