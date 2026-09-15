class MinStack:

    def __init__(self):
        self.data = []
        self.minNum = float("infinity")
        self.prefixMin = []

    def push(self, val: int) -> None:
        self.data.append(val)
        self.minNum = min(self.minNum, val)
        self.prefixMin.append(self.minNum)

    def pop(self) -> None:
        self.prefixMin.pop()
        self.minNum = self.top()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.prefixMin[-1]
