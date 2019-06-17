class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        result=[]
        
        def getRes(combination, digits_left):
            if len(digits_left)==0:
                result.append(combination)
            else:
                for letter in phone[digits_left[0]]:
                    getRes(combination+letter, digits_left[1:])
        
        if digits:
            getRes("",digits)
        return result
