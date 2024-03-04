# Q.12 Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# This would output an error because there only 2  parameters with default values and the first parameter does not have
# a default value.
# Also since there are no arguments being passed to the function this would cause an error because of the
# first parameter.
