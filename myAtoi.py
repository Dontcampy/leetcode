class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            i = 0
            positive = True
            num = 0
            maxInt = 2 ** 31 -1
            minInt = -(2 ** 31)
            try:
                while True:
                    if s[i] != " ":
                        break
                    i += 1
                if s[i] == "-":
                    positive = False
                    i += 1
                elif s[i] == "+":
                    i += 1
                while True:
                    pop = int(s[i])
                    if positive and (num > maxInt / 10 or (num == maxInt / 10 and pop > 7)):
                        return maxInt
                    elif positive is False and (num > (maxInt + 1) / 10 or (num == (maxInt + 1) / 10 and pop > 8)):
                        return minInt
                    else:
                        num = num * 10 + pop
                        i += 1
            except:
                pass
            return num if positive else -num
        else:
            return 0
        