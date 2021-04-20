from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,item):
        self.queue.appendleft(item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        return self.queue[-1]

if __name__ == "__main__":
    q = Queue()

    #binary number
    q.enqueue("1")
    for i in range(0,10):
        q.enqueue(q.front() + "0")
        q.enqueue(q.front() + "1")
        print(q.dequeue())
