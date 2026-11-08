class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # leftMult = [1] * len(nums)
        # rightMult = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     leftMult[i] =  leftMult[i - 1] * nums[i - 1]
        
        # for i in range(len(nums) - 2, -1, -1):
        #     rightMult[i] = rightMult[i + 1] * nums[i + 1]

        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     res[i] = leftMult[i] * rightMult[i]

        # return res

        res = [1] * len(nums)
        prefix = 1
        
        #left pass
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
            

        return res




