# Q.1 The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# The counter will cause an infinite loop of 0's. there was no increment placed to reach
# the number 5. Therefore counter < 5 always returns a truthy value.

