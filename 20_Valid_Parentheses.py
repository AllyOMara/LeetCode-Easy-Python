"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Odd length string can't pass
        len_str = len(s)
        if len_str % 2 != 0:
            return False

        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if stack == []:
                    return False
                if char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
        if stack == []:
            return True
        else:
            return False