class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        n = len(citations)
        
        while h < n and citations[h] > h:
            h += 1
        return h

