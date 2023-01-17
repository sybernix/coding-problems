class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q = [val] + self.q

    def pushMiddle(self, val: int) -> None:
        mid = len(self.q) // 2
        self.q = self.q[:mid] + [val] + self.q[mid:]

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        if (len(self.q) == 0):
            return -1
        front = self.q[0]
        self.q = self.q[1:]
        return front

    def popMiddle(self) -> int:
        if (len(self.q) == 0):
            return -1
        mid = len(self.q) // 2
        if (len(self.q) % 2 == 0):
            mid = mid - 1
        mid_num = self.q[mid]
        self.q = self.q[:mid] + self.q[mid+1:]
        return mid_num

    def popBack(self) -> int:
        if (len(self.q) == 0):
            return -1
        return self.q.pop()