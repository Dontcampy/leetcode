class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxInt = 2 ** 31 -1
        rev = 0
        positive = True
        if x < 0:
            positive = False
            x = -x
        
        while x != 0:
            pop = x % 10
            x = int(x / 10)
            if positive and (rev > maxInt / 10 or (rev == maxInt / 10 and pop > 7)):
                return 0
            elif positive is False and (rev > (maxInt + 1) / 10 or (rev == (maxInt + 1) / 10 and pop > 8)):
                return 0
            else:
                rev = rev * 10 + pop
        return rev if positive else -rev
