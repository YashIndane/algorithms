#Queue using stack

class Queue:
    def __init__(self, li:list):
        self.li = li
    
    def addElement(self, e):
        self.li.append(e)

    def pop(self):
        element = self.li[0]
        del self.li[0]
        return element

        
q = Queue([])   
q.addElement(3)
q.addElement(23)
q.addElement(-39) 

print(q.pop())
print(q.pop())
print(q.li)
