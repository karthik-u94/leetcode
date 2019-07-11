class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split(' ')
        words= [x for x in words if x!=""]
        # print(words)
        return ' '.join(words[::-1])
        
