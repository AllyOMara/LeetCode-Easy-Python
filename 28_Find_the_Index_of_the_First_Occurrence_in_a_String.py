"""
Given two strings 'needle' and 'haystack', return the index of the first
occurrence of 'needle' in 'haystack', or '-1' if 'needle' is not part of
'haystack'.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay = []
        nee = []
        for letter in haystack:
            hay.append(letter)
        for letter in needle:
            nee.append(letter)
        first_letter = nee[0]
        len_nee = len(nee)
        for i in range(len(hay) - len_nee + 1):
            letter = hay[i]
            if letter == first_letter:
                passes = True
                for j in range(len_nee):
                    if hay[i + j] != nee[j]:
                        passes = False
                if passes == True:
                    return i
        return -1