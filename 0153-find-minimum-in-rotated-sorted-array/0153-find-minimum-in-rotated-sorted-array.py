class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        for i in range(len(nums)):
            
            if nums[i] < min_val:
                min_val = nums[i]
        return min_val
            
        