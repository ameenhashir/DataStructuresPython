class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_first(self,data):
        if self.root:
            node = Node(data,self.root)
            self.root = node
        else:
            node = Node(data, None)
            self.root = node
        self.size+=1

    def insert_last(self,data):
        if self.size == 0:
            self.insert_first(data)
        else:
            itr = self.root
            prev = None
            while itr:
                prev = itr
                itr = itr.next
            node = Node(data,None)
            prev.next = node
            self.size+=1

    def print_all(self):
        if self.root:
            itr = self.root
            elements = []
            while itr:
                elements.append(itr.data)
                itr = itr.next
            elem_str = " --> ".join(str(elements).split(','))[1:-1]
            print(elem_str)
        else:
            print("Linked List Empty!!!")

    def get_length(self):
        print ("Size = ",self.size)

    def insert_values(self,elements):
        for elem in elements[::-1]:
            self.insert_first(elem)

    def insert_at(self,index,data):
        if index <0 or index >= self.size:
            raise Exception("Invalid Index")
        else:
            if self.root:
                itr = self.root
                prev = None
                count = 0
                while itr:
                    if count == index:
                        break
                    else:
                        prev = itr
                        itr = itr.next
                        count+=1
                node = Node(data,prev.next)
                prev.next = node

    def remove_at(self,index):
        if index <1 or index >= self.size:
            raise Exception("Invalid Index")
        else:
            if self.root:
                itr = self.root
                prev = None
                count = 0
                while itr:
                    if count == index:
                        break
                    else:
                        prev = itr
                        itr = itr.next
                        count+=1
                prev.next = itr.next

    def clear_list(self):
        self.root = None

    def insert_after_value(self,insert_after,data):
        itr = self.root
        while itr:
            if itr.data == insert_after:
                node = Node(data,itr.next)
                itr.next = node
            itr = itr.next

    def remove_by_value(self,data):
        itr = self.root
        prev = None
        while itr:
            if itr.data == data:
                if prev:
                    prev.next = itr.next
                else:
                    self.root = itr.next
            prev = itr
            itr = itr.next


if __name__=='__main__':
    ln = LinkedList()
    ln.insert_first(100)
    ln.insert_first(20)
    ln.insert_first(50)
    ln.insert_first(60)
    ln.print_all()
    ln.insert_values([4,6,3,9])
    ln.print_all()
    ln.insert_last(199)
    ln.print_all()
    ln.get_length()
    ln.insert_at(3,90)
    ln.print_all()
    #ln.clear_list()
    #ln.print_all()
    #ln.insert_at(0,90)
    #ln.print_all()
    ln.remove_at(5)
    ln.print_all()
    ln.insert_after_value(50,300)
    ln.print_all()
    ln.insert_after_value(199,400)
    ln.print_all()
    ln.remove_by_value(4)
    ln.print_all()
    ln.remove_by_value(50)
    ln.print_all()

    #execises
    print("--------------------------------------------exercise-----------------")
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_all()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print_all()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print_all()
    ll.remove_by_value("figs")
    ll.print_all()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_all()