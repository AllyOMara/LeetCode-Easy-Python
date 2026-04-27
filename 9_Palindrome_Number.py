"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):

        def check_palindrome(string):
            if len(string) < 1:
                return True
            if string[0] == string[-1]:
                return check_palindrome(string[1:-1])
            else:
                return False

        arr = []
        if x < 0:
            return False
        x = str(x)

        ans = check_palindrome(x)
        return ans
