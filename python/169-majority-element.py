from collections import defaultdict
# Time:  O(n)
# Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)

        for n in nums:
            m[n] += 1
        n = len(nums) // 2
        for k,v in m.items():
            if v > n:
                return k
        return 0
        