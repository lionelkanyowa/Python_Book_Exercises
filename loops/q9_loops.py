# Q.9 Write a function that computes and returns the factorial of a number by using a for or while loop. The factorial
# of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

#n!	Expansion	Result
#1!	1	1
#2!	1 * 2	2
#3!	1 * 2 * 3	6
#4!	1 * 2 * 3 * 4	24
#5!	1 * 2 * 3 * 4 * 5	120

def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1

    return result


print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))