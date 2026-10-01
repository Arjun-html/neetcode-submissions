class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 # first check
        stop = len(nums)-1 # final check

        while start <= stop:
            mid = start + ((stop - start) // 2) # midpoint of array
            if target == nums[mid]:
                return mid
            
            elif target < nums[mid]:
                stop = mid - 1

            elif target > nums[mid]:
                start = mid + 1

        return -1