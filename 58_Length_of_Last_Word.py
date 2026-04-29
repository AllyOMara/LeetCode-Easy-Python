"""
Given a string 's' consisting of words and spaces, return the length of the last
word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        def reverse(string):
            if len(string) == 1 or len(string) == 0:
                return string
            else:
                return string[-1] + reverse(string[:-1])
        rev = reverse(s)
        count = 0
        begin = False
        for char in rev:
            if begin == True:
                if char == " ":
                    return count
                else:
                    count += 1
            elif char != " " and begin == False:
                count += 1
                begin = True
        return count
