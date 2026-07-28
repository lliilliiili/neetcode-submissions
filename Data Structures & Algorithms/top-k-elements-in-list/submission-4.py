class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0)+1
        
        count_list = list(count.values())

        ans = []

        for i in range(k):
            maxcount = max(count_list)
            for j in count:
                if count[j] == maxcount:
                    ans.append(j)
                    count_list.remove(maxcount)
                    count.pop(j)
                    break

        return ans