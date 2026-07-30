class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        

        while i < j:
            num1 = numbers[i]
            num2 = numbers[j]
            if num1 + num2 == target:
                return [i+1, j+1]

            elif num1 + num2 < target:
                i += 1

            elif num1 + num2 > target:
                j -= 1

     
            
        