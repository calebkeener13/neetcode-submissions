class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        temp = [0] * 26
        res = []
        listMap = defaultdict(list)

        for word in strs:
            for c in word:
                temp[ord(c) - ord('a')] += 1

            listMap[tuple(temp)].append(word)
            temp[:] = [0] * 26

        for key, val in listMap.items():
            curr = []
            for word in val:
                curr.append(word)

            res.append(curr)

        return res

        


