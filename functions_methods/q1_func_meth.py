#Q1. What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'
    
set_foo()
print(foo)
    
#This program returns an 'NameError' letting us know that foo is not defined. In this case, foo is not in scope
#It is defined within the function, but not outise of it. 