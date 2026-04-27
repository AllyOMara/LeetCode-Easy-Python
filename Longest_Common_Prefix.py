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
            for string in strs:
                str_len = len(string)
                if smallest_len == None or smallest_len > str_len:
                    smallest_len = str_len

            if strs == []:
                return ""
            elif len(strs) == 1:
                return strs
            ans = []
            for string in strs:
                if string == "":
                    return ""
            for i in range(smallest_len):
                letter = strs[0][i]
                for string in strs:
                    if string[i] != letter:
                        return ans
                ans.append(letter)
        ans = find_prefix(strs)
        ans_str = ""

        if ans == []:
            return ""
        
        for letter in ans:
            ans_str = ans_str + letter
        return ans_str