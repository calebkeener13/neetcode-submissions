class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, val in counts.items():
            buckets[val].append(key)

        res = []
        for i in range(threshold + 1, len(nums) + 1):
            for n in buckets[i]:
                res.append(n)

        return res
        