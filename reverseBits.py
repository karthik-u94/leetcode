class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev = bin(n)[2:].zfill(32)[::-1]
        return int(rev,2)
        
