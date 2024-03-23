# Write a find_integers function that retuns a list of all integers from my_tuple:

def find_integers(num):
    return [number
            for number in num
            if type(number) is int]


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)
