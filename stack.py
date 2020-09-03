class Stack(object):
    def __init__(self,size=10):
        self.stack =  []
        self.size = size

    def stackTrace(self):
        """
            Prints all elements of the Stack
        """
        print([x for x in self.stack])


    def push(self,element):
        """
            Push/Insert a new element into the Stack.
        """
        if len(self.stack) >= self.size:
            print("Stack Full!!")
        else:    
            self.stack.append(element)

    def pop(self):
        """
            Pops/deletes the topmost element in the Stack.
        """
        if len(self.stack) <= 0:
            print("Stack Empty!!")
        else:
            self.stack.pop()    

    def getTop(self):
        """
            Returns topmost element from the Stack without deleting it. 
        """
        print(self.stack[len(self.stack)-1])

    def isEmpty(self):
        """
            Returns True if the Stack is Empty. 
        """
        if len(self.stack) == 0:
            return True
        else:
            return False    

s = Stack(2)
s.pop()
s.push(50)
s.push(45)
s.push(88)
s.getTop()
s.stackTrace()
s.pop()
s.stackTrace()
s.getTop()
    