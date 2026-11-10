class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCounts = defaultdict(int)
        prefixCounts[0] = 1
        res = 0

        prefix = 0
        for n in nums:
            prefix += n
            diff = prefix - k

            res += prefixCounts[diff]
            prefixCounts[prefix] += 1

        return res

        


