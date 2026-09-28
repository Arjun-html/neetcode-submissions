class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_t = {}
        for i in range(len(t)):
            if t[i] not in list_t:
                list_t.update({t[i] : 1})
            else:
                list_t[t[i]] += 1
        list_s = {}
        for i in range(len(s)):
            if s[i] not in list_s:
                list_s.update({s[i] : 1})
            else:
                list_s[s[i]] += 1

        if list_s == list_t:
            return True
        else: return False
        
        
