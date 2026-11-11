class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # lets enforce this so i < j < k
        nums.sort()

        res = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                sums = nums[j] + nums[k]
                if sums > target:
                    k -= 1
                elif sums < target:
                    j += 1
                else:
                    if (nums[i], nums[j], nums[k]) not in res:
                        res.add((nums[i], nums[j], nums[k]))

                    j += 1
                    k -= 1
        return [list(triplet) for triplet in res]
                        
