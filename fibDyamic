class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        two = 0
        one = 1
        for i in range(1, N):
            new = two+one
            two = one
            one = new
        return one
