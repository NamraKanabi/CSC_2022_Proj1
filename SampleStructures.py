class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):       
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Index out of range")
    
    def peek(self):      
        try:
            return self.items[len(self.items)-1] 
        except IndexError:
            raise IndexError("Index out of range")
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        if len(self.items)==0:
            pass
        else:
            self.items.clear()