class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l, r = 0, len(heights) - 1

        while l < r:
            most = max(min(heights[l], heights[r]) * (r - l), most)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1 

        return most
        