class Solution:
    def countAndSay(self, n):
        return self.countAndSayHelper('1#', 2, n)
        
    def countAndSayHelper(self, prev_result, current_iteration, n):
        if current_iteration > n:
            return prev_result[:-1]
        result = ''
        count = 1
        for i in range(1, len(prev_result)):
            if prev_result[i] == prev_result[i-1]:
                count += 1
            else:
                result += str(count) + prev_result[i-1]
                count = 1
        return self.countAndSayHelper(result + '#', current_iteration + 1, n)
