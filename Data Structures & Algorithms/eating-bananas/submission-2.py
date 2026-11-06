class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort array piles 
        # biggest index 
        # if h == len(piles), answer is max(piles)
        # if h < len(piles), find the smallest (n - h) subgroups no overlap 
        # if h > len(piles), find the biggest (n-h) and divide 
        # arrays cant be sorted 
        left, right = 1, max(piles)
        ret = right

        while left <= right:
            mid = (right + left) // 2
            ans = 0
            for pile in piles:
                ans += (-(-pile // mid))

            if ans <= h:
                right = mid - 1
                ret = mid
            else:
                left = mid + 1

        return ret



        