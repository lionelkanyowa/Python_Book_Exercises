# Q11. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# The output will be the following:
# 42
# 3
# 2

# As we can see, the method passes 3 parameters as arguments, and we see that there is only 1 argument passed.
# However, we output 3 arguments. This is because the function still gets invoked without its arguments
# second = 3 and third = 2 is a default parameter.