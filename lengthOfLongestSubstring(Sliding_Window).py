class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySet = {}
        maxLen, i, j =0, 0, 0
        while j < len(s):
            if s[j] in mySet:
                # 如果已包含此字符，则将i赋值为此字符的位置+1, 注意不要比原i还小的值
                i = max(i, mySet[s[j]] + 1)
            mySet[s[j]] = j
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen
# s = Solution()
# print(s.lengthOfLongestSubstring("tmmzuxt"))
# print(s.lengthOfLongestSubstring("dvdf"))
