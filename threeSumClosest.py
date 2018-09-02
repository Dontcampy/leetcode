class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minM = 0
        closest = target
        for n in range(0, len(nums) - 2):
            if n != 0 and nums[n] == nums[n-1]: # 如果n重复直接推进
                continue
            si, i = n + 1, n + 1
            sj, j = len(nums) - 1, len(nums) - 1
            while i < j:
                s = nums[n] + nums[i] + nums[j]
                if s == target:
                    return target
                elif s > target or (j != sj and nums[j] == nums[j + 1]): 
                    m = s - target
                    if minM == 0 or m < minM:
                        minM = m
                        closest = s
                    j -= 1
                elif s < target or (i != si and nums[i] == nums[i - 1]): 
                    m = target - s
                    if minM == 0 or m < minM:
                        minM = m
                        closest = s
                    i += 1

        return closest
