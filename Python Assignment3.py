"""1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()"""


# reduce() function in python has takes in 3 arguments viz. (function, iterable, initializer). Default value of initializer is set as None


def myreduce(funct, seq, initial=None):
    if initial is None:
        seq1 = iter(seq)
        extractor = next(seq1)
    else:
        extractor = initial

    for item in seq:
        extractor = funct(extractor, item)
    return extractor


# Example:
def add(x, y):
    return x + y


print(myreduce(add, [1, 2, 3, 4, 5]))

"""1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()"""


# filter() function in python has takes in 2 arguments viz. (function, iterable).

def myfilter(func1, seq1):
    result = []
    for item1 in seq1:
        if func1(item1) is True:
            result.append(item1)
    return result


# Example:
def is_odd(n):
    return n % 2 != 0


print(myfilter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists

a = ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
b = ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
c = [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]
d = [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]"""

a = [item * i for item in ['x', 'y', 'z'] for i in range(1, 5)]
print(a, end='\n')

b = [item * i for i in range(1, 5) for item in ['x', 'y', 'z']]
print(b, end='\n')

c = [[i + j] for i in range(2, 5) for j in range(3)], [[i + j for i in range(4)] for j in range(2, 6)]
c = c[0] + c[1]
print(c, end='\n')

d = [(i, j) for j in range(1, 4) for i in range(1, 4)]
print(d, end='\n')
