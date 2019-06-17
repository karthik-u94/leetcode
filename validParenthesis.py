class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        paraList=[]
        for i in range(len(s)):
            if(s[i]=='{' or s[i]=='(' or s[i]=='['):
                paraList.append(s[i])
            if (s[i]=='}' or s[i]==']' or s[i]==')') and len(paraList)==0:
                return False
            if(s[i]=='}'):
                if(paraList[-1]=='{'):
                    paraList.pop()
                else:
                    return False
            elif(s[i]==']'):
                if(paraList[-1]=='['):
                    paraList.pop()
                else:
                    return False 
            elif(s[i]==')'):
                if(paraList[-1]=='('):
                    paraList.pop()
                else:
                    return False 
        if(len(paraList)!=0):
            return False
        return True
