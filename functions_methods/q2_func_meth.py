#Q2. Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'
    
set_foo()
print(foo)

#What does this program print and why?

#The program will print 'bar' because the variable outside the function is the one being initialized.
#The method still gets called but it is the variable outside the function that is initialized and printed.
