class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0 
        res = 0
        freqMap = defaultdict(int)
        maxFreq = 0

        while r < len(s):
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            while r - l + 1 - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res


            
        


        