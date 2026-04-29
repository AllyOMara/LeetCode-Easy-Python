"""
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            len_nums = len(nums)
            if nums[0] > target:
                return 0
            elif nums[len_nums - 1] < target:
                return len_nums
            else:
                for i in range(len_nums - 1):
                    num = nums[i]
                    if num < target and nums[i + 1] > target:
                        return i + 1
                        