"""Assignment 2"""

"""Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""

char = "*"
n = 2
for i in range(0, 2 ** n + 1):
    print((char * i) + char)
for j in range(0, 2 ** n):
    print(char * (2 ** n - j))

"""Write a Python program to reverse a word after accepting the input from the user"""

word = str(input("Enter a word:"))
for i in range(0, len(word)):
    print(word[len(word) - i - 1], end='')
