class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}

        for n in  nums:
            map[n] = map.get(n, 0)+1

        bucket = [[] for _ in range(len(nums)+1)]

        for val, count in map.items():
            bucket[count].append(val)

        ans = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                ans.append(num)
            if len(ans) == k:
                return ans
