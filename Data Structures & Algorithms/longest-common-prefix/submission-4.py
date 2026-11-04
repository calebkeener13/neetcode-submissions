class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""

        for i in range(len(strs[0])):
            target = strs[0][i]
            for word in strs:
                if len(res) == len(word) or word[i] != target:
                    return res
            res += target

        return res