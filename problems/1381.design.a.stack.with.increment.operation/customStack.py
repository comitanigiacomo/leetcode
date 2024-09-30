class CustomStack:
    
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(len(self.stack)):
            if i < k: 
                self.stack[i] += val
