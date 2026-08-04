class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c not in check:
                stack.append(c)
            
            else:
                if stack and stack[-1] == check[c]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        else:
            return True