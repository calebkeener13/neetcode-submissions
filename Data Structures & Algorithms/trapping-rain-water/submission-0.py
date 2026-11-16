class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n

        for i in range(n):
            if i == 0:
                maxLeft[i] = height[i]
                continue

            maxLeft[i] = max(height[i], maxLeft[i - 1])

        for i in range(n - 1, -1 , -1):
            if i == n - 1:
                maxRight[i] = height[i]
                continue

            maxRight[i] = max(height[i], maxRight[i + 1])

        res = 0
        for i in range(len(height)):
            res += min(maxLeft[i], maxRight[i]) - height[i]

        return res
