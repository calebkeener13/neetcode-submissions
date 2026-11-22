class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLen = len(s)
        if len(t) > len(s):
            return res

        # set for equality info does not give us enough information, so lets try a counts
        target = Counter(t)
        counts = defaultdict(int)
        matches = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] in target:
                if counts[s[r]] == target[s[r]] - 1:
                    matches += 1

                counts[s[r]] += 1


            while matches == len(target):
                if r - l + 1 <= minLen:
                    minLen = r - l + 1
                    res = s[l: r + 1]

                if s[l] in target:
                    counts[s[l]] -= 1
                    print(counts[s[l]])
                    if counts[s[l]] + 1 == target[s[l]]:
                        matches -= 1

                l += 1  
            r += 1  

        return res
        