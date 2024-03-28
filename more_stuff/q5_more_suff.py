# Q.5 On reflection, we've decided that we don't want to rely on using a global variable in the code we wrote in the previous example. 
# To fix this, we're going to nest the code from the previous example into an outer function:

# There's a bug in this code. Identify the bug, and fix it.

def all_actions():
    counter = 0
    
    def increment_counter():
        nonlocal counter
        counter += 1
        
    print(counter)
    
    increment_counter()
    print(counter)
    
    increment_counter()
    print(counter)
    
    counter = 100
    increment_counter()
    print(counter)
    
all_actions()
