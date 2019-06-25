class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moveCounts=collections.Counter(moves)
        return moveCounts['L']==moveCounts['R'] and moveCounts['U']==moveCounts['D']
