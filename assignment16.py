class queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue==[]:
            print("queue is empty")

        else:
            self.queue.pop(0)

#display queue
    def display(self):
        print("queue:",list(self.queue))

q=queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("dequeued element:",q.safe_deqeue())
print("dequeued element:",q.safe_deqeue())
print("dequeued element:",q.safe_deqeue())

print("dequeued element: ",q.safe_dequeue())

