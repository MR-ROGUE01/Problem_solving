class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        nums.sort()

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,n-1):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l =  n - 1

                while k < l:
                    total_sum = nums[i] + nums[j] + nums[k] + nums[l]

                    if total_sum < target:
                    
                        k += 1

                    elif total_sum > target:
                        l -= 1

                    else:
                        temp = [nums[i], nums[j], nums[k],nums[l]]
                        ans.append(temp)

                    # Move both pointers
                    
                        k += 1
                        l -= 1

                    # Skip duplicate j
                        while k < l and nums[k] == nums[k - 1]:
                        
                            k += 1

                    # Skip duplicate k
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return ans
        