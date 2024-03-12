class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_dict and nums_dict[compliment] != i:
                return [i, nums_dict[compliment]]
        



        
