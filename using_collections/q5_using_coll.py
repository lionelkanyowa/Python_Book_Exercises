# Q.5 Which of the following values can't be used as a key in a dict object and why?

'cat'
(3, 1, 4, 1, 5, 9,
['a', 'b'] # Cannot be used; a list is muatble
{'a': 1, 'b':2} # Cannot be used; a dict is mutable
range(5)
{1, 4, 9, 16, 25} # Cannot be used; a set is mutable
3
0.0
frozenset({1, 4, 9, 16, 25})

