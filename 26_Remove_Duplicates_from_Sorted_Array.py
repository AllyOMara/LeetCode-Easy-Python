"""
Given an integer array 'nums' sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same.

Consider the number of unique elements in 'nums' to be 'k'. After removing
duplicates, return the number of unique elements 'k'.

The first 'k' elements of 'nums' should contain the unique numbers in sorted
order. The remaining elements beyond index 'k - 1' can be ignored.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 1
        i = 0
        
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            elif nums[i] != nums[i + 1]:
                i += 1
        return len(nums)