class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1 or len(s) == 0:
        #     return len(s)

        # positions = defaultdict(int)
        # res = 0
        # l,r = 0, 0

        # while r < len(s):
        #     curr = s[r]
        #     if curr not in positions:
        #         positions[curr] = r
        #     else:
        #         res = max(res, r - l)
        #         l = positions[curr] + 1
        #         positions[curr] = r

        #     r += 1
                
        # res = max(res, r - l)
        # return res

        if len(s) == 1 or len(s) == 0:
            return len(s)

        seen = set()
        res = 0
        l,r = 0, 0
        while r < len(s):
            if s[r] in seen:
                res = max(res, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1

            seen.add(s[r])
            r += 1

        res = max(res, r - l)
        return res
            
        