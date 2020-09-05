class Queue(object):
    def __init__(self,length=10):
        self.queue = []
        self.length = length
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQ(self,element):
        """
            Inserts element at the rear of queue.
        """
        if self.size >= self.length :
            print("Queue full!!")
        else:
            self.queue.insert(self.rear,element)
            self.rear += 1
            self.size += 1 

    def deQ(self):
        """
            Removes element from the front of queue.
        """
        if self.size <= 0:
            print("Queue Empty!!")
        else:
            self.queue.pop(self.front)
            self.size -= 1
            self.rear -= 1


    def printQ(self):
        """
            Prints Queue elements.
        """
        print([x for x in self.queue])

    def getSize(self):
        """
            Returns the size of Queue.
        """
        return self.size

q = Queue(5)
q.enQ(20)
q.enQ(12)
print(q.getSize())
q.printQ()
q.deQ()
q.printQ()


