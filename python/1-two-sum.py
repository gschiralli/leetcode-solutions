class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            nums_dict[nums[i]] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict and nums_dict[complement] != i:
                return [i, nums_dict[complement]]
        



        
