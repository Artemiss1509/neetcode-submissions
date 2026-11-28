class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ''
        for i in strs:
            en+=str(len(i))+"."+i
            #print(en)
        return en

    def decode(self, s: str) -> List[str]:
        de = []

        i = 0
        while i < len(s):
            dot = s.find('.', i)
            length = int(s[i:dot])
            de.append(s[dot + 1:dot + 1 + length])
            i = dot + 1 + length
            
        return de
