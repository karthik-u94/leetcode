class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        stone_count=collections.Counter(S)
        for j in J:
            if(stone_count.get(j)):
                count+=stone_count.get(j)
        return count
