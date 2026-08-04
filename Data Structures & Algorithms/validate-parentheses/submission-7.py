class Solution:
    def isValid(self, s: str) -> bool:
        
        check = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in check:
                if stack and check[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if not stack:
            return True 
        else:
            return False