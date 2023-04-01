# create a function that returns True if the given string is palindrome, False otherwise. 
# Palindrome means that string equals its reversed version. 
# The function should not be case sensitive. 
# 
# Examples: 
# HannaH -> palindrome -> True
# Hannah -> palindrome -> True

def ispalindrome(word):
    # I need to reversed version of given string
    reversed = word[::-1]
    # we could match the case of two words
    return reversed.lower() == word.lower()

word = input("Enter a word")

print(ispalindrome(word))