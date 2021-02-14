class Node:
    def __init__(self,data = None,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.root = None
        self.tail = None
        self.size = 0

    def insert(self,data):
        if self.root:
            node = Node(data, None, self.root)
            self.root.prev = node
            self.root = node
        else:
            node = Node(data,None,None)
            self.root = node
            self.tail = node

    def insert_values(self,elements):
        for elem in elements[::-1]:
            self.insert(elem)

    def print_forward(self):
        elements = []
        itr = self.root
        while itr:
            elements.append(itr.data)
            itr = itr.next
        print(str(elements))

    def print_backward(self):
        elements = []
        itr = self.tail
        while itr:
            elements.append(itr.data)
            itr = itr.prev
        print(str(elements))


if __name__=="__main__":
    ln = DoublyLinkedList()
    ln.insert_values([1,2,3,4,5,6])
    ln.print_forward()
    ln.print_backward()