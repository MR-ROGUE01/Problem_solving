class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in nums:
                x = num
                curr = 1
                while x + 1 in nums:
                    curr += 1
                    x += 1
                longest = max(longest,curr)
        return longest