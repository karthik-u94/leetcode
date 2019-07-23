class Solution:
    def intToRoman(self, num: int) -> str:
        values={
            1:'I',
            5:'V',
            4:'IV',
            9:'IX',
            10:'X',
            50:'L',
            40:'XL',
            100:'C',
            90:'XC',
            500:'D',
            1000:'M',
            400:'CD',
            900:'CM'
        }
        factors=sorted(values.keys())
        res=""
        
        i=len(factors)-1
        while num>0:
            while num//factors[i]==0:
                i-=1
            res+=values[factors[i]]*(num//factors[i])
            num=num%factors[i]
        
        return res
