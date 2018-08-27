class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxSet = set()
        for i in range(0, len(s)):
            interSet = set(s[i])
            for j in range(i + 1, len(s)):
                if j and s[j] not in interSet:
                    interSet.add(s[j])
                else:
                    break
            if len(maxSet) < len(interSet):
                maxSet = interSet
        return len(maxSet)
