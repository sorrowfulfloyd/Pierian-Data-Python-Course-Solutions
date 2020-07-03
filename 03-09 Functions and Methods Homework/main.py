# Functions and Methods Homework

# 1: Write a function that computes the volume of a sphere given its radius.

# Formula: V(olume) = 4/3 pi x**3

from math import pi
import string

def vol(r):
    return (4/3 * pi * r**3)
    # Using the pi from math instead of 3.14 to give more accurate solution.

# print(vol(2))

# 2: Write a function that checks whether a number is in a given range (inclusive of high and low)

def numCheck(n,l,h):
    if n < h and n > l:
        return (f"{n} is in the range between {l} and {h}")
    else:
        return (f"{n} is not in range between {l} and {h}")

# print(numCheck(4,1,5))

# or returning a boolean

def numCheckBool(n,l,h):
    return n < h and n > l

# print(numCheckBool(6,1,5))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def upANDlow(st):
    d = {'UPPER': 0, 'LOWER': 0}
    for i in st:
        if i.isupper():
            d['UPPER'] += 1
        elif i.islower():
            d['LOWER'] += 1
    return (f'That string has {d["UPPER"]} upper and {d["LOWER"]} lower characters')

# print(upANDlow("Hello Mr. Rogers, how are you this fine Tuesday?"))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list(set(lst))

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.

def multi(nums):
    result = 1
    for i in nums:
        result *= i
    return result

# print(multi([1,2,3,-4]))

# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(st):
    if len(st) < 3:
        return st
    nStr = st.replace(' ', '')
    return nStr[::-1].lower() == nStr.lower()

# print(palindrome('damad'))

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

def isPangram(st, alphabet = string.ascii_lowercase):
    newSt = st.replace(' ', '')
    return set(newSt).issuperset(set(alphabet))

# print(isPangram("The quick brown fox jumps over the lazy dog"))

# EZ CLAP