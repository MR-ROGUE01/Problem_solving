class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subset = []
        result = []

        def solve(ind, subset):
            if ind >= len(nums):
                result.append(subset.copy())
                return

            # Include current element
            subset.append(nums[ind])
            solve(ind + 1, subset)

            # Exclude current element
            subset.pop()
            solve(ind + 1, subset)

        solve(0, subset)
        return result