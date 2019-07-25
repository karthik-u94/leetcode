class Solution:
    def numberToWords(self, num: int) -> str:
        num_dict={
            0:"Zero",
            1:"One",
            2:"Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12:"Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen",
            20:"Twenty",
            30:"Thirty",
            40:"Forty",
            50:"Fifty",
            60:"Sixty",
            70:"Seventy",
            80:"Eighty",
            90:"Ninety",
            100:"Hundred",
            1000:"Thousand",
            1000000:"Million",
            1000000000:"Billion"
        }
        if len(str(num))==1:
            return num_dict[num]
        
        
        keys=sorted(num_dict.keys())
        pre=[100,1000,1000000,1000000000]
        
        def helper(num, i):
            temp=""
            while num>0:
                
                while (num//keys[i])==0:
                    i-=1
                t=num//keys[i]
                if t not in num_dict or keys[i] in pre:
                    temp+=helper(t,i)+" " + num_dict[keys[i]]+" "
                else:
                    temp+=num_dict[keys[i]]+" "
                global res
                num=num%keys[i]
            return temp.strip()
        
        return helper(num,len(keys)-1)
            
