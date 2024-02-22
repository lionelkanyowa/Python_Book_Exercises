#Q7. What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# Code outputs the greeting of Victor 3 times then the greeting of Nina 3 times. 
#The Constant Variable NAME is first assigned to 'Victor' on line 3, then
#reassigned to 'Nina' on line8.
#Since python does not have real constants, for best practices you should not re-assign variables 
#written in constant form.