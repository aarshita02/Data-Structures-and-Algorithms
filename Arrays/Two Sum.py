  
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lib ={}
        for i,n in enumerate(nums):
            if n in lib:
                return[lib[n], i]
            lib[target-n]= i
        return[]
 
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].
