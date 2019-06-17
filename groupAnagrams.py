class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=collections.defaultdict(list)
        
        for str in strs:
            res[tuple(sorted(str))].append(str)
        return res.values()
        
