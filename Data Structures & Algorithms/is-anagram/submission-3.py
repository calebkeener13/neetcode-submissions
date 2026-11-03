class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        temp = defaultdict(int)

        for c in s:
            temp[c] += 1

        for c in t:
            temp[c] -= 1
            if temp[c] == 0:
                temp.pop(c)
        
        if len(temp) > 0:
            return False

        return True

        