class queue:
    def __init__(self, size=10):
        self.size = size
        self.queue = list()

    def inqueue(self, value):
        if len(self.queue) == self.size:
            print('full')
            return
        else:
            self.queue.append(value)

    def dequeue(self, ):
        if not self.queue:
            print('empty')
            return
        else:
            return self.queue.pop(-1)