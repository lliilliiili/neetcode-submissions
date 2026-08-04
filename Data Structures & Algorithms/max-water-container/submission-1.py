class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxans = 0 

        while l < r:
            limit = min(heights[l], heights[r])
            length = r - l
            maxans = max(maxans, limit*length)

            if heights[l] < heights[r] :
                l += 1
            else:
                r -= 1

        return maxans