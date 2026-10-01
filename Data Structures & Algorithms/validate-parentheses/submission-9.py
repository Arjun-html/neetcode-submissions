class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}', '[':']', '(':')'}
        p_seen = []
        for i in s:
            if i in dic:
                p_seen.append(i) # opening bracket
            elif i in dic.values():
                if not p_seen:
                    return False
                elif i == dic[p_seen[-1]]: # matching end found
                    p_seen.pop()
                else: return False
            
        
        return not p_seen # true if everything got closed
        