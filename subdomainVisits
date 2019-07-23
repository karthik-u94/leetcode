class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_counts={}
        
        for dom in cpdomains:
            temp=dom.split(' ')
            visits=int(temp[0])
            # print(dom.split(' ')[1])
            subs=temp[1].split('.')
            for i in range(len(subs)):
                ip='.'.join(subs[i:])
                if ip in visit_counts:
                    visit_counts[ip]+=visits
                else:
                    visit_counts[ip]=visits
        res=[]
        for k in visit_counts.keys():
            res.append(str(visit_counts[k])+" "+k)
        return res
