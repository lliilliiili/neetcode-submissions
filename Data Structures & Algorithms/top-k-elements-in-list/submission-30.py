class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}

        for s in nums:
            res[s] = res.get(s, 0) + 1

        ansList = [[] for _ in range(len(nums)+1)]

        for num, count in res.items():
            ansList[count].append(num)

        ans = []

        for i in range(len(ansList)-1, 0, -1):
            for j in ansList[i]: 
                ans.append(j)
                if len(ans) == k :
                    return ans
                