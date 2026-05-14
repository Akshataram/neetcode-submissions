class MinStack:

    def __init__(self):
        self.stack=[]
        self.s1=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        else:
            return

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return

    def getMin(self) -> int:
        min=float('inf')
        while self.stack:
            a=self.stack.pop()
            if a<min:
                min=a
            self.s1.append(a)
        while self.s1:
            self.stack.append(self.s1.pop())
        return min


        
