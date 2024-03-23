# Q.2 Without running this code, what will it print? Why?

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)


# This would print the following:
# {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}
# set1 and set2 are the same and have the same address in memory.
# If an element is added to set1, it is also added to set2 vice versa.
