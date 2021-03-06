class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            for i in range(0, len(strs[0])):
                for j in range(0, len(strs)):
                    if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                        return strs[0][0:i]
            return strs[0]
        else:
            return ""
