class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l, r = 0, 0
        currSum = 0
        minLen = float("inf")
        while r < len(nums):
            currSum += nums[r] 
            while currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum -= nums[l]
                l += 1

            r += 1
        
        if minLen == float("inf"):
            return 0

        return minLen

            

        