class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        temp = [0] * 26
        listMap = defaultdict(list)

        for word in strs:
            for c in word:
                temp[ord(c) - ord('a')] += 1

            listMap[tuple(temp)].append(word)
            temp[:] = [0] * 26

        return list(listMap.values())

        


