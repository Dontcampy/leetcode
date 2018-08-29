class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s:
            for length in range(len(s), 0, -1): # 遍历所有子字符串
                for i in range(0, len(s) - length + 1): 
                    new_str = s[i:i + length]
                    if self.isPalindrome(new_str):
                        return new_str
        else:
            return ""
    
    def isPalindrome(self, s):
        """判断字符串是否为回文
        """
        begin, end = 0, len(s) - 1
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True
