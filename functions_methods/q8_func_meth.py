# Q.9 Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)


foo(42, 3.141592, 2.718)

# This would raise an error. The original method has 2 parameters to be passed as arguments in line 1.
# However, 3 arguments are passed in line 7.


