class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = res.get(i, 0)+1
        
        orderList = sorted(res.keys(), key = res.get, reverse = True)

        ans = []
        for num in orderList:
            if len(ans) == k :
                return ans
            ans.append(num)
        return ans