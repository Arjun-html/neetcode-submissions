class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i in range(len(nums)):
            y = target - nums[i] 
            if y in h:
                return [h[y], i]
            h[nums[i]] = i
