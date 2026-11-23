class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        D = dict.fromkeys(s,0)
        for i in s:
            D[i]+=1
        for k in t:
            if k in D:
                D[k]-=1
            else:
                return False
        return not any(D.values())
    
