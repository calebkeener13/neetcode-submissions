class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        buckets = [[] for _ in range(len(nums) + 1)]

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        for key, val in counts.items():
            buckets[val].append(key)


        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            

        return res


