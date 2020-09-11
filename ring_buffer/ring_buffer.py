class RingBuffer:
    def __init__(self, capacity, x=0):
        self.capacity = capacity
        self.data = []
        self.x = x
    def append(self, item):
        if self.capacity == len(self.data):
            self.data.pop(self.x)
            self.data.insert(self.x, item)
            self.x += 1
            if self.x >= self.capacity:
                self.x = 0
        else:
            self.data.insert(len(self.data), item)

    def get(self):
        return self.data