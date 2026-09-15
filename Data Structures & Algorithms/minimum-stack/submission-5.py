class MinStack:

    def __init__(self):
        self.data = []
        self.prefixMin = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.prefixMin:
            val = min(val, self.prefixMin[-1])
        self.prefixMin.append(val)

    def pop(self) -> None:
        self.prefixMin.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.prefixMin[-1]
