class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d = []
        s = []
        for e in logs:
            _id, word = e.split(' ')[:2]
            if word.isdigit():
                d.append(e)
            else:
                s.append((e, e.replace(_id+' ', '')+' '+_id))
        s = [x[0] for x in sorted(s, key=lambda x: x[1])]
        print(s)
        return s+d
