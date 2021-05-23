"""
217. Contains Duplicate
"""
class Solution:
    def containsDuplicate(self, nums) -> bool:
        numset = set(nums)
        if len(numset) != len(nums):
            return True
        else:
            return False

sol1 = Solution()
print(sol1.containsDuplicate([1, 2, 3, 4, 1]))