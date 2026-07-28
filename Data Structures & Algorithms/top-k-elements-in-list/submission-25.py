class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = res.get(i, 0)+1
        
        orderList = sorted(res.keys(), key = lambda x:res[x], reverse = True)

        return orderList[:k]