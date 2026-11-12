class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        boatNum = 0
        while l < r:
            weight = people[r] + people[l]

            if weight <= limit:
                l += 1
            
            boatNum += 1
            r -= 1

        if l == r:
            return boatNum + 1

        return boatNum
        