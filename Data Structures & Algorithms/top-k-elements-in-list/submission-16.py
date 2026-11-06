class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        buckets = [[] for _ in range(len(nums) + 1)]

        counts = defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                buckets[1].append(num)
                counts[num] += 1

            else:
                buckets[counts[num]].remove(num)
                counts[num] += 1
                buckets[counts[num]].append(num)


        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                res.append(num)
            
            if len(res) == k:
                break

        return res


