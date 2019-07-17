class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(para):
            stack=[]
            for p in para:
                if p=='(':
                    stack.append(p)
                else:
                    if len(stack)!=0  and stack[-1]=='(':
                        stack.pop()
                    else:
                        stack.append(p)
            
            return len(stack)==0
        
        def get_combination(current, rem_open, rem_close):
            if rem_open==0 and rem_close==0:
                if isValid(current):
                    results.append(current)
            else:
                if rem_open>0:
                    get_combination(current+'(', rem_open-1, rem_close )
                if rem_close>0:
                    get_combination(current+')', rem_open, rem_close-1 )
        results=[]
        get_combination("", n,n)
        return results
                
