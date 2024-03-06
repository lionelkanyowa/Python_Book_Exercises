# Q.5 What does this code output and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')


is_list_empty([])

# This would output 'Empty' The method invokes an empty array collection in line 10  which is also regarded
# as a falsy value, and since the else statement represents a false the program would print 'Empty'
