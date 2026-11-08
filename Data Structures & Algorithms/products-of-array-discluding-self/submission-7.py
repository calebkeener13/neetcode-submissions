class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMult = [1] * len(nums)
        rightMult = [1] * len(nums)

        for i in range(1, len(nums)):
            rightIndex = len(nums) - 1 - i
            leftMult[i] =  leftMult[i - 1] * nums[i - 1]
            rightMult[rightIndex] = rightMult[rightIndex + 1] * nums[rightIndex + 1]


        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = leftMult[i] * rightMult[i]

        return res