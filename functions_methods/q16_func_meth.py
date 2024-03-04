# Q.16 In the code shown below, identify all the function names and parameters present in the code.
# Include the line numbers for each item identified.

def multiply(left, right):
    return left * right


def get_num(prompt):
    return float(input(prompt))


first_number = get_num('Enter first number: ')
second_number = get_num('Enter second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names:
# multiply(line 4, 14), get_num (line 8, 12,13)
# input(line 9), float(line9), print(line15)

# Parameters
# left, right (line 4, 5)
# prompt (line 8)
