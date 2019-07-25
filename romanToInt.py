class Solution:
    def romanToInt(self, s: str) -> int:
        values={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if len(s)==1:
            return values[s]
        pairs={
            'I':['V','X'],
            'X':['C','L'],
            'C':['D','M']
        }
        i,j=0,1
        val=0
        while i<len(s):
            if s[i] in pairs:
                if i+1<len(s) and s[i+1] in pairs[s[i]]:
                    val+=values[s[i+1]]-values[s[i]]
                    i+=2
                else:
                    val+=values[s[i]]
                    i+=1
            elif i<len(s):
                val+=values[s[i]]
                i+=1
        return val
            
