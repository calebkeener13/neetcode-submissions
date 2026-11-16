class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        maxLeft[0] = height[0]
        maxRight[-1] = height[-1]

        for i in range(1, n):
            j = n - 1 - i
            maxLeft[i] = max(height[i], maxLeft[i - 1])
            maxRight[j] = max(height[j], maxRight[j + 1])

        res = 0
        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i]

        return res
