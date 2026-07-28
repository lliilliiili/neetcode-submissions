class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums :
            res[i] = res.get(i, 0) + 1

        ansList = [[] for _ in range(len(nums)+1)]

        for num, count in res.items():
            ansList[count].append(num)

        ans = []
        for i in range(len(ansList)-1, 0, -1):
            for n in ansList[i]:
                if len(ans) == k:
                    return ans
                ans.append(n)
        return ans
