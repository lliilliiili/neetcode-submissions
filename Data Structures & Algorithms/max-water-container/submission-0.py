class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        max = 0
        
        while l < r:
            limit = min(heights[l],heights[r])
            length = r-l
            if limit * length > max :
                max = limit * length
                
            if heights[l] == limit:
                    l +=1
            else:
                    r -= 1
        
        return max

