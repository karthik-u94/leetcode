class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen=set()
        
        for n in A:
            if n not in seen:
                seen.add(n)
            else:
                return n
