class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        removed = False
        rBackup, lBackup = 0,0

        while l < r:
            if removed:
                if s[lBackup] != s[r] and s[rBackup] != s[l]:
                    return False
                elif s[lBackup] == s[r] and s[rBackup] != s[l]:
                    lBackup += 1
                    r -= 1
                    continue
                elif s[lBackup] != s[r] and s[rBackup] == s[l]:
                    rBackup -= 1
                    l += 1
                    continue
            else:
                if s[l] != s[r]:
                    rBackup = r - 1
                    lBackup = l + 1
                    removed = True
                    continue
                    
            l, r = l + 1, r - 1
            lBackup, rBackup = lBackup + 1, rBackup -1
        
        return True
            
        