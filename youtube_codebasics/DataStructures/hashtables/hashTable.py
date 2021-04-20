class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for x in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for ch in key:
            h+=ord(ch)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][index] = (key,value)
                found = True
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, item):
        h = self.get_hash(item)
        found = False
        for index,elements in enumerate(self.arr[h]):
            if elements[0] == item:
                return elements[1]
                found = True
        if not found:
            return -1

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index,elements in enumerate(self.arr[h]):
            if elements[0] == key:
                del self.arr[h][index]

if __name__ == "__main__":
    h = HashTable()
    h['march 6'] = 100
    h['march 6'] = 200
    h['march 9'] = 300
    h['march 17'] = 400
    print(h['march 17'])
    del h['march 17']
    print(h['march 17'])
    print(h.arr)