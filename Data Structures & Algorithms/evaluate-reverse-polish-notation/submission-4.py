class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        cacul = 0
        for c in tokens:
            if c not in "+-*/":
                stack.append(c)
            else:
                num1 = int(stack[len(stack)-2])
                num2 = int(stack[-1])
                if c == '+':
                    cacul = num1 + num2
                    stack.pop()
                    stack.pop()
                    stack.append(str(cacul))
                elif c == '-':
                    cacul = num1 - num2
                    stack.pop()
                    stack.pop()
                    stack.append(str(cacul))
                elif c == '*':
                    cacul = num1 * num2
                    stack.pop()
                    stack.pop()
                    stack.append(str(cacul))
                elif c == '/':
                    cacul =int(num1 / num2)
                    stack.pop()
                    stack.pop()
                    stack.append(str(cacul))

        ans = int(stack[0])
        return ans
