class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set(nums)
        res = 1
    
        for i in range(len(nums)):
            if nums[i] - 1 not in seen:
                #this means it must start a sequence
                curr = nums[i]
                temp = 1
                while curr + 1 in seen:
                    temp += 1
                    if temp > res:
                        res = temp

                    curr += 1
        return res


        
        