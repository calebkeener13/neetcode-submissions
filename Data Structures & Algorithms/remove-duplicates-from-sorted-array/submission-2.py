class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 0
        w = 0

        while r < len(nums):
            if w == 0 or nums[r] > nums[w -1]:
                nums[w] = nums[r]
                w +=1
            r += 1

        return w


                
        