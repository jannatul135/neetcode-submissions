class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        intput : list of numbers 
        output : boolean, true or false if there is a dublicate 

        plan : 
        - pointer 1 pointer 2 
        - loop through nums as pointer 1
        - loop through nums after pointer 1 as pointer 2
        - check if pointer 1 matches pointer 2 
        - if it doesn't return false
        -  otherwhise pointer 1 ++
        '''


        # pointer1 = 0
        # check = {}
        # while pointer1 < len(nums):
        #     pointer2 = pointer1+1
        #     while pointer2<len(nums):
        #         if nums[pointer1] == nums[pointer2]:
        #             return True
        #         else:
        #             pointer2 = pointer2+1
        #     pointer1 = pointer1 + 1
        # return False

        '''
        - initialize set
        - look through nums
        - if current number is not in the set
        - add the current number in the set
        -otherwise return true
        '''

        check = set()

        for current in nums:
            if current not in check:
                check.add(current)
            else:
                return True
        return False


