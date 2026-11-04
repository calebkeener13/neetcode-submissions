class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        maxLen = 200
        for word in strs:
            if len(word) < maxLen:
                maxLen = len(word)

        for i in range(maxLen):
            target = strs[0][i]
            for word in strs:
                if word[i] != target:
                    return res
            res += target

        return res