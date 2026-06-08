from collections import deque

class MonotonicDeque:

    def __init__(self):
        self.dq = deque()

    def push(self, value):

        while self.dq and self.dq[-1] < value:
            self.dq.pop()

        self.dq.append(value)

    def max(self):

        if not self.dq:
            return None

        return self.dq[0]

    def pop(self, value):

        if self.dq and self.dq[0] == value:
            self.dq.popleft()