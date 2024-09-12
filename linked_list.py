class ListNode:
    def __init__(self, data):
        self.__value = data
        self.next = None

    @property
    def value(self, ):
        return self.__value
    
    @value.setter    
    def set_value(self, new):
        self.__value = new 
    
class LinkedList:
    def __init__(self, ):
        self.head = None
        self.tail = None

    def add(self, data):

        new = ListNode(data)    
        if self.head == None:
            self.head = new
        
        else:
            self.tail.next = new

        self.tail = new

    def delete(self, value):
        
        current = self.head

        while current != None:
            if current.value == value:
                
        