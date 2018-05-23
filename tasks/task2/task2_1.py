"""
Write a program that check whether a string is palindrome or Not.
To check code you can use strings
from https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes
def isPalindrome(str):
"""
input_str = input('Введите строку: ')

input_str = input_str.casefold()

rev_str = reversed(input_str)[:input_str: -1]

if list(input_str) == list(rev_str):

    print("It is palindrome")

else:

    print("It is not palindrome")
