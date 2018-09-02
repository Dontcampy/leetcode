class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            phone_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
            com = [s for s in phone_dict[digits[0]]]

            for s in digits[1:]:
                com = [m + n for m in com for n in phone_dict[s]]
            return com
        else:
            return []
            