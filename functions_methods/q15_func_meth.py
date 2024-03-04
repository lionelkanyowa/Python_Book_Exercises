# Q.15 Using the code below, classify the identifiers as global, local, or built-in. For our purposes,
# you may assume this code is the entire program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# All identifiers

# multiply 3,13 (global)
# left, right 3,4 (local
# get_num 7 (global)
# prompt 7, 8 (local)
# float 8 (built-in)
# input 8 (built-in)
# first_number 11, 13, 14 (global)
# second_number 12, 13, 14 (global)
# product 13, 14 (global)
# print 14 (built-in)


