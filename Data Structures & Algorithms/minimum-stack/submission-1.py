class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack or val<= self.ministack[-1]:
            self.ministack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.ministack[-1]:
            self.ministack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ministack[-1]
