class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
                total = max(curr,total)
            else:
                curr = 0
        return total
            

        