"""
1. Two Sum
"""

class Solution:
    def twoSum(self, nums, target):
       nummap = {}
       for i in range(len(nums)):
            num = nums[i]
            if target - num in nummap:
                return [nummap[target - num], i]
            nummap[num] = i

sol1 = Solution()
print(sol1.twoSum([3,2,4], 6))
        