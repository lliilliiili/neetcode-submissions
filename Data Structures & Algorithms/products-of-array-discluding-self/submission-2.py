class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = {}

        for i in range(len(nums)):
            res[i] = nums[i]

        ans = []

        allproduct = 1
        avoid = False
        count = 0
        
        if 0 not in nums:
            for n in res:
                allproduct *= res.get(n)

            for n in res:
                ans.append(int(allproduct)//res.get(n))
            
            return ans

        if 0 in nums:
            for n in res:
                
                if res.get(n) == 0 and count == 0 :
                    count += 1
                    continue
                else:
                    avoid = True
                    allproduct *= res.get(n)

            for n in res:
                if avoid:
                    if res.get(n) != 0 :
                        ans.append(0)
                    else:
                        ans.append(allproduct)
                else:
                    ans.append(0)
            
            return ans
