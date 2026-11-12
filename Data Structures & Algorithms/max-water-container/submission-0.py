class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l, r = 0, len(heights) - 1

        while l < r:

            temp = min(heights[l], heights[r]) * (r - l)
            if temp > most:
                most = temp

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1 

        return most
        