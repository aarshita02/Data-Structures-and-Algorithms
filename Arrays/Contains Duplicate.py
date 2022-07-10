"""
Three possible solutions
"""

# First Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
      
      
# Second Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                return True
            else:
                dictionary[i] = 1
        return False
      
# Third Solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
