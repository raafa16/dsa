class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            # the floor division // rounds the result down to the nearest whole number
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
