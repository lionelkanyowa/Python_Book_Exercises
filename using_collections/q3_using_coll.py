# Q.3 Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from
# the original. It should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)

my_list.reverse()

print(tuple(my_list[1:4]))

