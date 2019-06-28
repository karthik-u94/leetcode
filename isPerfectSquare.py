class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x=math.sqrt(num)
        return ((math.floor(x)-x)==0)
