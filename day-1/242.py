"""
242. Valid Anagram
"""

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        charmap = {}
        for chr in s:
            if chr in charmap:
                charmap[chr] += 1
            else:
                charmap[chr] = 1
        for chr in t:
            if chr in charmap and charmap[chr] < 0:
                return False
            elif chr in charmap:
                charmap[chr] -= 1
            else:
                return False
        # for key in charmap:
        #     if charmap[key] != 0:
        #         return False
        # return True

sol1 = Solution()
print(sol1.isAnagram('aacc', 'ccac'))

        