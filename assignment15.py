class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)

    def safe_pop(self):
        if self.stack!=[]:
            self.stack.pop()
        
        else:
            print("stack is empty")

    def display(self):
        print("stack:",self.stack)
        
s=stack()

s.push(70)
s.push(80)
s.push(90)

s.display()

print("popped element:",s.safe_pop())
print("popped element:",s.safe_pop())
print("popped element:",s.safe_pop())

print("popped element:",s.safe_pop())
