class stack:
    
    def __init__(self, size=float("inf")):
        self.element = list()
        self.size = size

    def push(self, value):
        if not self.isFull():
            self.element.insert(0, value)
        
        else:
            print('full')

    def pop(self,):
        if not self.isEmpty():
            self.element.pop()
        else:
            print('empty')

    def isFull(self):
        if len(self.element) >= self.size:
            return True
        
        return False
    
    def isEmpty(self):
        if not self.element:
            return True
        
        return False
    
