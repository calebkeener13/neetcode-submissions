class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set(nums)
        res = 1
    
        for start in seen:
            if start - 1 not in seen:
                #this means it must start a sequence
                curr = start
                temp = 1
                while curr + 1 in seen:
                    temp += 1
                    if temp > res:
                        res = temp

                    curr += 1
        return res


        
        