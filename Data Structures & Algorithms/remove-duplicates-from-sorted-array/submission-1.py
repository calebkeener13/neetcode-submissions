class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()

        r = 0
        w = 0

        while r < len(nums):
            if nums[r] not in seen:
                print("here")
                nums[w] = nums[r]
                w += 1

            seen.add(nums[r])
            r += 1

        return w


                
        