class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        sums = set()
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                c = b + 1
                d = len(nums) - 1
                con = nums[a] + nums[b]
                while c < d:
                    temp = nums[c] + nums[d] + con 
                    if temp > target:
                        d -= 1
                    elif temp < target:
                        c += 1
                    else:
                        sums.add((nums[a], nums[b], nums[c], nums[d]))

                        c += 1
                        d -= 1
        return [list(s) for s in sums]