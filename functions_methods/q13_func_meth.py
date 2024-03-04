# Q13. Without running the code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# This would output an error because there is only 1 parameter with a default value and the third parameter
# does not have a default value nor is there an argument passed to the function for it.
