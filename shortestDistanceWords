class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = -1, -1
        shortestDist = len(words) - 1
        for i in range(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1:
                shortestDist = min(shortestDist, abs(idx1 - idx2))
                
                #since 1 is the min distance, we can stop & return
                if shortestDist == 1:
                    return shortestDist
        
        return shortestDist
