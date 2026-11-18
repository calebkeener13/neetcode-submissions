class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        l, r = 0, 1
        while l < len(nums) - 1:
            if nums[l] == nums[r]:
                return True
            else:
                if r - l < k and r < len(nums) - 1:
                    r += 1
                else:
                    l += 1
                    r = l + 1

        return False
