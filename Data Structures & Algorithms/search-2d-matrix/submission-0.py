class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        midrow = 0

        while top <= bottom:
            midrow = top + (bottom - top)//2
            if target < matrix[midrow][0]:
                bottom = midrow - 1
            elif target > matrix[midrow][-1]:
                top = midrow + 1
            else:
                break

        if not (top <= bottom):
            return False

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) //2 
            if matrix[midrow][mid] > target:
                right = mid  - 1
            elif matrix[midrow][mid] < target:
                left = mid + 1
            else:
                return True
        return False 

