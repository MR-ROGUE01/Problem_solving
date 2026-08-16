class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        n = len(nums)

        nums.sort()

        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1

                elif total_sum > 0:
                    k -= 1

                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return [list(x) for x in ans]