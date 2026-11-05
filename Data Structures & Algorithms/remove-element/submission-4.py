class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            while l <= r and nums[l] == val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r -= 1
            
            l += 1

        return r+1