class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pToS = defaultdict(int)
        for i in range(len(position)):
            pToS[position[i]] = speed[i]

        position.sort()
        for i in range(len(position)):
            speed[i] = pToS[position[i]]

        time = [0] * len(position)
        for i in range(len(position)):
            time[i] = (target - position[i]) / speed[i] 

        res = 1
        leader = -1
        for i in range(len(position) - 2, -1, -1):
            if time[i] > time[leader]:
                res += 1
                leader = i
        
        return res

        