class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        res = {}
        for n in nums:
            res[n] = res.get(n, 0) + 1
        
        
        maxans = 1

        for key in res:
            ans = 1
            pt = key
            while pt+1 in res:
                ans +=1
                pt +=1
            if ans> maxans:
                maxans = ans
        
        return maxans