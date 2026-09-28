class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        a2 = set()
        for num in nums:
            if num in a2:
                return True
            a2.add(num)
        return False