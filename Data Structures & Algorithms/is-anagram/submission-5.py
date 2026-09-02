class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False        
        
        sFreq = {}
        tFreq = {}

        for i in range(len(s)):
            if s[i] in sFreq.keys():
                sFreq[s[i]] += 1
            else:
                sFreq[s[i]] = 1

            if t[i] in tFreq.keys():
                tFreq[t[i]] += 1
            else:
                tFreq[t[i]] = 1
        
        if sFreq == tFreq:
            return True
        
        return False



       