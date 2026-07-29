class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxans = 0
        for n in numset:

            if n-1 not in numset:
                ans = 1
                while n+ans in numset:
                    ans +=1
                
                maxans = max(maxans, ans)
            
        return maxans

        