class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""

        for i in range(len(strs[0])):
            target = strs[0][i]
            for word in strs:
                if i == len(word) or word[i] != target:
                    return strs[0][:i]



        return strs[0]