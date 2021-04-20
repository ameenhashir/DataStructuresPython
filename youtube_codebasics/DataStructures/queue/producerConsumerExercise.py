import time as t
from collections import deque
import threading


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


class Orders:
    def __init__(self):
        self.q = Queue()

    def placeOrder(self, orders):
        for order in orders:
            self.q.enqueue(order)
            #print('Placed : ',order)
            t.sleep(0.5)
        print('Place Order Completed!!!')

    def serveOrder(self):
        while not self.q.is_empty():
            print('Served : ',self.q.dequeue())
            t.sleep(0.5)
        print('Serve Order Completed!!!')


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    ord = Orders()

    #multi threading
    t1 = threading.Thread(target=ord.placeOrder,args=(orders,))
    t2 = threading.Thread(target=ord.serveOrder)

    t1.start()
    t.sleep(0.5)
    t2.start()

    t1.join()
    t2.join()

    print('All Done!!!')
