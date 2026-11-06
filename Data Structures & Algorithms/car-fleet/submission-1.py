class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = {}
        n = len(position)
        for i in range(n):
            cars[position[i]] = (target - position[i]) / speed[i]
        # {position: arrival time}
        # sort positions 
        position.sort()
        
        ans = 0
        t = 0

        for p in range(n - 1, -1, -1):
            # print(cars)
            # print(cars[position[p]])
            # print(cars[position[p + 1]])
            if cars[position[p]] > t:
                ans += 1
                t = cars[position[p]]
        return ans

        

        