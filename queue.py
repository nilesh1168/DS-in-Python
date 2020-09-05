class Queue(object):
    def __init__(self,length=10):
        self.queue = []
        self.length = length
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQ(self,element):
        if self.size >= self.length :
            print("Queue full!!")
        else:
            self.queue.insert(self.rear,element)
            self.rear += 1
            self.size += 1 

    def deQ(self):
        if self.size <= 0:
            print("Queue Empty!!")
        else:
            self.queue.pop(self.front)
            self.size -= 1
            self.rear -= 1


    def printQ(self):
        print([x for x in self.queue])

    def getSize(self):
        return self.size

q = Queue(5)
q.enQ(20)
q.enQ(12)
print(q.getSize())
q.printQ()

