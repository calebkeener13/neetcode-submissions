class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l, r = 1, x // 2
        curr = 0
        while l <= r:
            mid = (r + l) // 2
            print(mid)
            if x // mid > mid:
                l = mid + 1
                curr = mid
            elif x // mid < mid:
                r = mid - 1
            else:
                return mid

        return curr
        
        