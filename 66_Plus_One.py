"""
You are given a large integer represented as an integer array 'digits', where
each 'digits[i]' is the 'ith' digit of the integer. The digits are ordered from
most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        last = len(digits) - 1
        digits[last] += 1
        while digits[last] == 10:
            if last != 0:
                digits[last] = 0
                last -= 1
                digits[last] += 1
            else:
                digits[last] = 0
                digits.insert(0, 1)
        return digits