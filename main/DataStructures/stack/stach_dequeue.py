from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self,elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__=="__main__":
    s = Stack()
    s.push(5)
    print(s.stack)
    print(s.pop())
    #s.pop()
    print(s.is_empty())
    s.push(15)
    s.push(25)
    s.push(35)
    print(s.size())
