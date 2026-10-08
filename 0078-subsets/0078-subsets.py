class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result_set = []
        n = len(nums)
        total = 1<<n
        for num in range(0,total):
            lst = []
            for i in range(0,n):
                if num & (1<<i) != 0:
                    lst.append(nums[i])
            result_set.append(lst)
        return result_set 
        