"""
Given an array of integers 'nums' and an integer 'target', return indices of the
two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        other_nums = {}  # {other_number, first index}
        ans = []
        for i in range(len(nums)):
            number = nums[i]
            other_num = target - number
            if other_num not in other_nums:
                other_nums.update({number: i})
            elif other_num in other_nums:
                ans.append(other_nums[other_num])
                ans.append(i)
                return ans
        return None
