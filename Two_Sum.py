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
