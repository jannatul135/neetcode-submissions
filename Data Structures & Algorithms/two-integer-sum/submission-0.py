class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for left in range(len(nums)):
            for right in range (left+1, len(nums)):
                if nums[left]+nums[right] == target:
                    return [left,right]
'''
        left = 0
        right = len(nums)-1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left,right]
            left = left + 1
            right = right - 1
'''



        
