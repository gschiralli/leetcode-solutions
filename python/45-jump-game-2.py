class Solution:
    def jump(self, nums):
        reach, jumps, last = 0, 0, 0
        
        for i in range(len(nums)-1):    
            
            reach = max(reach, i + nums[i])
        
            if i == last:
                last = reach      
                jumps += 1
        return jumps
        
