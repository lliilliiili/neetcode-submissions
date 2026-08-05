class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [[] for _ in range(len(temperatures))]
        res = []
        for i in range(len(temperatures)):
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)

            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    ans[stack[-1]].append(i - stack[-1])
                    stack.pop()
                stack.append(i)
            
        for i in stack:
            ans[i].append(0)

        
        for l in ans:
            for c in l:
                res.append(c)
        return res