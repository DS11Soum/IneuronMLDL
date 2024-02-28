""" Assignment 1"""

"""Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line."""

for num in range(1999, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=',')

"""Write a Python program to accept the user's first and last name and then getting them 
printed in the the reverse order with a space between first name and last name."""

first_name = str(input("Enter First Name:"))
last_name = str(input("Enter Last Name:"))
name = first_name + " " + last_name
for i in range(0, len(name)):
    print(name[len(name) - i - 1], end='')

"""Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r 3"""

pi = 22 / 7
r = (12 / 100)

volume = (4 / 3)
print(volume)
