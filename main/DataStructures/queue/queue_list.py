class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.insert(0,item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

if __name__=='__main__':
    q = Queue();
    q.enqueue(10)
    q.enqueue(100)
    print(q.queue)
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    print(q.is_empty())