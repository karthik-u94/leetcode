class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        temp = []
        out = []
        k = 0
        
        for index,i in enumerate(S):
            if len(temp)>=1:
                out.append(S[index])
            if i == '(':
                temp.append(i)
                
            else:
                temp.pop()
            # print(temp)
            
            if len(temp) == 0:
                out.pop()
        
        return ''.join(out)
                    
