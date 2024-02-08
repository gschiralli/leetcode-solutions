# # Time:  O(n)
# # Space: O(n)
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         k = 0
#         dup_dict = {}

#         for i in range(len(nums)):
#             if nums[i] not in dup_dict:
#                 nums[k] = nums[i]
#                 k += 1
#                 dup_dict[nums[i]] = 1
#             elif nums[i] in dup_dict and dup_dict.get(nums[i],0) < 2:
#                 nums[k] = nums[i]
#                 k += 1
#                 dup_dict[nums[i]] = dup_dict.get(nums[i],0) + 1
#         return k
    
#Improved solution
# Time:  O(n)
# Space: O(1)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        occurrence = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                occurrence += 1
            else:
                occurrence = 1
            if occurrence <= 2:
                nums[k] = nums[i]
                k+=1
        return k