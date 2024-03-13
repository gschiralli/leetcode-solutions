class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_cpy = ["".join(sorted(s)) for s in strs]
        anagram_dict = dict()
        for i in range(len(strs)):
            if strs_cpy[i] in anagram_dict:
                anagram_dict[strs_cpy[i]].append(strs[i])
            else:
                anagram_dict[strs_cpy[i]] = [strs[i]]
                

        return anagram_dict.values()
        
