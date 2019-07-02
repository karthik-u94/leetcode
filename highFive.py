class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores={}
        
        for score in items:
            if score[0] not in scores.keys():
                scores[score[0]]=[score[1]]
            else:
                scores[score[0]].append(score[1])
        res=[]
        for stu in scores.keys():
            scores[stu]=sorted(scores[stu],reverse=True)
            res.append([stu,sum(scores[stu][:5])/5])

        return res
        
