class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for n in range(0, len(nums) - 2):
            if n != 0 and nums[n] == nums[n-1]: # 如果n重复直接推进
                continue
            si, i = n + 1, n + 1
            sj, j = len(nums) - 1, len(nums) - 1
            while i < j:
                s = nums[n] + nums[i] + nums[j]
                if s > 0 or (j != sj and nums[j] == nums[j + 1]): # 如果和大于0或则j重复则j - 0
                    j -= 1
                elif s < 0 or (i != si and nums[i] == nums[i - 1]): # 如果和小于0或则j重复则i - 0
                    i += 1
                else:
                    res.append([nums[n], nums[i], nums[j]])
                    i += 1
                    j -= 1
        return res
