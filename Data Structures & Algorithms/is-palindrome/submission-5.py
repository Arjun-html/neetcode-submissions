class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [a.lower() for a in s if a.isalnum()]
        return t == t[::-1]
            