class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        if s:
            for center in range(0, len(s)):
                len1 = self.expandAroundCenter(s, center, center) # 单字符为中心
                len2 = self.expandAroundCenter(s, center, center + 1) # 双字符为中心
                if len1 >= len2 and len1 > (end - start):
                    start = center - int(len1 / 2)
                    end = center + int(len1 / 2)
                elif len1 < len2 and len2 > (end - start):
                    start = center - int(len2 / 2)
                    end = center + 1 + int(len2 / 2)
            return s[start:end + 1]
        else:
            return ""

    def expandAroundCenter(self, s, left, right):
        """中心扩展
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left <= 1:
            return 0
        else:
            return right - left - 2 # 因为此处right和left是下一次检查的索引，所以要-2纠正
