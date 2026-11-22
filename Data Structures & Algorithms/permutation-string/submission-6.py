class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        b1 = [0] * 26
        b2 = [0] * 26

        ## build the buckets array for s1 and the starting window for s2
        for i in range(len(s1)):
            b1[ord(s1[i]) - ord('a')] += 1
            b2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if b1[i] == b2[i]:
                matches += 1

        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            # increment r and add its char
            newChar = ord(s2[i]) - ord('a')
            b2[newChar] += 1
            if b2[newChar] - 1 == b1[newChar]:
                matches -= 1
            if b2[newChar] == b1[newChar]:
                matches += 1

            # increment l and remove its char count
            oldChar = ord(s2[i - len(s1)]) - ord('a')
            b2[oldChar] -= 1
            if b2[oldChar] + 1 == b1[oldChar]:
                matches -= 1
            if b2[oldChar] == b1[oldChar]:
                matches += 1

            # check if matches == 26

            if matches == 26:
                return True

        return False

        