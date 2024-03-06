# Q.6 Write a program that takes a string as an argument and returns an all caps version of the string when the
# string is longer than 10 characters. Otherwise, it should return the original string.
# Example: change 'hello world' to 'Hello WORLD', but don't change 'goodbye'

def word(string):
    if (len(string)) > 10:
        return string.upper()
    else:
        return string


print(word('hello world'))
print(word('example'))
print(word('Launch School is awesome!'))
