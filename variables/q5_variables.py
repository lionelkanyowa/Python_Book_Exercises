#Q5. Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string value 'Victor' 
# in each greeting. Here's an example run of the program:

name = 'Victor'

print('Good Morning, ' + name+'.')
print('Good Afternoon, ' +name+'.')
print('Good Evening, ' + name+'.')

# This solution uses f-string interpolation
name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')