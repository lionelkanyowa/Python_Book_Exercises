# Q10. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# This would output the following:
# 42,
# 3.141592
# 2

# As we can see, the method passes 3 parameters as arguments, and we see that there are only 2 arguments passed.
# However, we output 3 arguments. This is because the function still gets invoked without its arguments
# third = 2 is a default parameter.
