class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]

        stack = []
        maxrec = 0  

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                maxrec = max(maxrec, h*w)

            stack.append(i)

        return maxrec