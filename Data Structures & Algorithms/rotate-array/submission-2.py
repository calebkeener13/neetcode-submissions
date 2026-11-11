class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # ## reverse the full array
        # nums = nums[::-1]

        # ## reverse first part
        # nums[:k] = nums[:k][::-1]

        # ## reverse back half
        # nums[k:] = nums[k:][::-1]

        i, j = 0, len(nums) - 1
        rot = k % len(nums)
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = 0, rot - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = rot, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]

            i += 1
            j -= 1

        
        