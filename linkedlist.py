class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        """
            Prints the contents of the List.
        """
        if self.head == None:
            print("List is empty!!")
        else:
            temp = self.head
            while temp != None:
                print(temp.value)
                temp = temp.next    
        print("End of list")



    def insertAtEnd(self,value):
        """
            Appends given value at the end of the List.
        """
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            print("inside else")
            temp = self.head
            while temp.next != None:
                temp = temp.next
                print("in while")
            temp.next = newNode    

    def insertAtStart(self,value):
        """
            Appends given value at the start of the List.
        """
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            newNode.next = temp
            self.head = newNode


    def insertBefore(self,nodeValue,value):
        """
            Adds node before the given nodeValue.
        """
        newNode = Node(value)
        if nodeValue == self.head.value:
            self.insertAtStart(value)
        else:
            temp = self.head
            while temp:
                if temp.next.value == nodeValue:
                    break
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode


    def insertAfter(self,nodeValue,value):
        """
            Adds node before the given nodeValue.
        """
        newNode = Node(value)
        temp = self.head
        while temp:
            if temp.value == nodeValue:
                break
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode            

    def deleteNode(self,value):
        """
            Deletes the given node from the list
        """
        temp = self.head
        while temp:
            if temp.next.value == value:
                break
            temp = temp.next
        temp.next = temp.next.next    



l = LinkedList()
l.insertAtEnd(2)
l.insertAtEnd(4)
l.insertAtStart(1)
l.printList()
l.insertBefore(1,20)
l.printList()
l.insertAfter(1,30)
l.printList()
l.deleteNode(30)
l.printList()