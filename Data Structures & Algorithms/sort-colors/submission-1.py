class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        curr = 0

        while curr <= r:
            if nums[curr] == 0:
                temp = nums[curr]
                nums[curr] = nums[l]
                nums[l] = temp

                curr += 1
                l += 1
            elif nums[curr] == 2:
                    temp = nums[curr]
                    nums[curr] = nums[r]
                    nums[r] = temp

                    r -= 1
            else:
                curr += 1

        
            