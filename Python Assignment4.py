"""1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass."""



class area_of_tr:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
       
    def areatf(self):
        s = (self.a + self.b + self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return area   
    
m = area_of_tr(int(input()), int(input()), int(input()))

print(m.areatf())


"""1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n."""

def filter_long_words(n,seq):
   r =  [item for item in seq if len(item)>n]
   return r

print(filter_long_words(5, ['alpha', 'beta', 'bvsbaks']))


"""2.1 Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] Here 2,3 and 4 are the lengths of the words in the list."""


def length_of_words(seq1):
   res =  [len(item1)for item1 in seq1]
   return res

print(length_of_words(['alph', 'bta', 'bvsbs']))


"""2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""


def filter_vowels(char):
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    return char in list_vowels

print(filter_vowels('b'))
