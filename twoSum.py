class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        while len(nums) > 1:
            n1 = nums.pop()
            for i in range(0, len(nums)):
                if nums[i] + n1 == target:
                    return [i, len(nums)]
