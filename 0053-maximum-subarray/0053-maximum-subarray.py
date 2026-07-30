class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            
            if total < 0:
                total = 0
                
            total += nums[i]
            maxi = max(maxi,total)
        return maxi