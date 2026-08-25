class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lb(nums,target):
            n = len(nums)
            l = 0
            r = n - 1
            lb = -1
            while l <= r:
                mid = (l + r)// 2
                if nums[mid] >= target:
                    lb = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return lb

        def ub(nums,target):
            n = len(nums)
            l = 0
            r = n - 1
            ub = -1
            while l <= r:
                mid = (l + r)// 2
                if nums[mid] > target:
                    ub = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return ub

        first = lb(nums,target)
        if first == -1 or nums[first] != target:
            return [-1,-1]
        last = ub(nums,target)
        if last == -1:
            last = len(nums)
        return [first,last - 1]
                    