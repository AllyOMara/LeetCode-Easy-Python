"""
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def find_prefix(strs):
            
            smallest_len = None
            ans = []

            for string in strs:
                str_len = len(string)
                if smallest_len == None or smallest_len > str_len:
                    smallest_len = str_len
            
            # Base cases
            if smallest_len == 0:
                return ans
            elif strs == []:
                return ""
            elif len(strs) == 1:
                for letter in strs[0]:
                    ans.append(letter)
                return ans

            # Solving
            for i in range(smallest_len):
                letter = strs[0][i]
                for string in strs:
                    if string[i] != letter:
                        return ans
                ans.append(letter)

            return ans

        # Converting solution into correct format
        ans = find_prefix(strs)
        ans_str = ""

        if ans == []:
            return ""
        else:
            for letter in ans:
                ans_str = ans_str + letter

        return ans_str