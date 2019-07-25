class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split('.')
        v2=version2.split('.')
        p1,p2=0,0
        
        while p1<len(v1) or p2<len(v2):
            v1_c,v2_c=0,0
            if p1<len(v1):
                v1_c=int(v1[p1])
               
            if p2<len(v2):
                v2_c=int(v2[p2])
                
            if v1_c>v2_c:
                return 1
            elif v2_c>v1_c:
                return -1
            else:
                p1+=1
                p2+=1
        
        return 0
            
            
