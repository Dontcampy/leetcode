class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        r = []
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for key in d:
            if d[key] == 1:
                r.append(key)
        return r
        